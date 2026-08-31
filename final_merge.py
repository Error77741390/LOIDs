#!/usr/bin/env python3

# Read Remendy mod
with open('/workspace/Remendy mod.txt', 'r') as f:
    remendy = f.read()

# Read Main mod  
with open('/workspace/Main mod.txt', 'r') as f:
    main_mod = f.read()

# Extract hat and acc functions from Main mod
hat_start = main_mod.find('function hat(id) {')
if hat_start != -1:
    brace_count = 0
    start_brace = main_mod.find('{', hat_start)
    for i in range(start_brace, len(main_mod)):
        if main_mod[i] == '{':
            brace_count += 1
        elif main_mod[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                hat_end = i + 1
                break
    hat_func = main_mod[hat_start:hat_end]
else:
    hat_func = ''

acc_start = main_mod.find('function acc(id) {')
if acc_start != -1:
    brace_count = 0
    start_brace = main_mod.find('{', acc_start)
    for i in range(start_brace, len(main_mod)):
        if main_mod[i] == '{':
            brace_count += 1
        elif main_mod[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                acc_end = i + 1
                break
    acc_func = main_mod[acc_start:acc_end]
else:
    acc_func = ''

# Extract isBoughtHat function
isBoughtHat_start = main_mod.find('function isBoughtHat(')
if isBoughtHat_start != -1:
    brace_count = 0
    start_brace = main_mod.find('{', isBoughtHat_start)
    for i in range(start_brace, len(main_mod)):
        if main_mod[i] == '{':
            brace_count += 1
        elif main_mod[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                isBoughtHat_end = i + 1
                break
    isBoughtHat_func = main_mod[isBoughtHat_start:isBoughtHat_end]
else:
    isBoughtHat_func = ''

# Extract UTILS object
utils_start = main_mod.find('let UTILS = {')
if utils_start != -1:
    brace_count = 0
    start_brace = main_mod.find('{', utils_start)
    for i in range(start_brace, len(main_mod)):
        if main_mod[i] == '{':
            brace_count += 1
        elif main_mod[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                utils_end = i + 1
                break
    utils_obj = main_mod[utils_start:utils_end]
else:
    utils_obj = ''

# Extract hatFc function
hatFc_start = main_mod.find('function hatFc() {')
if hatFc_start != -1:
    brace_count = 0
    start_brace = main_mod.find('{', hatFc_start)
    for i in range(start_brace, len(main_mod)):
        if main_mod[i] == '{':
            brace_count += 1
        elif main_mod[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                hatFc_end = i + 1
                break
    hatFc_func = main_mod[hatFc_start:hatFc_end]
else:
    hatFc_func = ''

print(f"Extracted hat: {len(hat_func)} chars")
print(f"Extracted acc: {len(acc_func)} chars")
print(f"Extracted isBoughtHat: {len(isBoughtHat_func)} chars")
print(f"Extracted UTILS: {len(utils_obj)} chars")
print(f"Extracted hatFc: {len(hatFc_func)} chars")

# Find insertion point in Remendy - after storeEquip definitions
insert_marker = 'globalThis.storeBuy = function(id, index)'
insert_pos = remendy.find(insert_marker)

if insert_pos == -1:
    print("ERROR: Could not find insertion point")
    exit(1)

# Create the hat system code to insert
hat_system_code = f'''
// ========== X- PRECISION HAT SYSTEM ==========
{hat_func}

{acc_func}

{isBoughtHat_func}

{utils_obj}

{hatFc_func}
// ========== END X- PRECISION HAT SYSTEM ==========

'''

# Insert the hat system
merged_content = remendy[:insert_pos] + hat_system_code + remendy[insert_pos:]

# Now find updateGame and add hatFc call
updateGame_marker = 'globalThis.updateGame = function()'
updateGame_pos = merged_content.find(updateGame_marker)

if updateGame_pos != -1:
    # Find the opening brace of updateGame
    brace_pos = merged_content.find('{', updateGame_pos)
    # Insert hatFc call at the beginning of updateGame, after variable declarations
    # Look for the first major section comment or after initial setup
    insert_hatfc_pos = merged_content.find('// MOVE CAMERA:', updateGame_pos)
    
    if insert_hatfc_pos != -1:
        # Insert hatFc call before MOVE CAMERA section
        hatfc_call = '''
    // X- PRECISION HAT SYSTEM CALL
    if (window.xHatSystemEnabled) {
        try {
            hatFc();
        } catch(e) { console.log("Hat error:", e); }
    }
    
'''
        merged_content = merged_content[:insert_hatfc_pos] + hatfc_call + merged_content[insert_hatfc_pos:]
        print("Added hatFc() call to updateGame")
    else:
        print("WARNING: Could not find MOVE CAMERA section")
else:
    print("WARNING: Could not find updateGame function")

# Add config variables at the top after the header
header_end = merged_content.find('==/UserScript==')
if header_end != -1:
    config_code = '''
// ==/UserScript==

// X- PRECISION HAT SYSTEM CONFIGURATION
window.xHatSystemEnabled = true;  // Set to false to disable hat system

// Variables needed by hatFc (will be populated by game state)
window.currentHat = 6;
window.nearestEnemy = null;
window.myPlayer = null;
window.predictWeapon = 0;
window.primaryReload = [];
window.secondaryReload = [];
window.turretReload = [];
window.autoBreak = false;
window.antiPush = false;
window.autogathering = false;
window.shouldResetShame = false;
window.imTrapped = false;
window.spikeDmgCount = 0;
window.spikeTickAnti = false;
window.insta = {primary: false, secondary: false, primaryturret: false, turret: false};
window.ePress = false;
window.autoaim = false;
window.leftClick = false;
window.soldierAnti = false;
window.nearestTrap = null;

'''
    merged_content = merged_content[:header_end] + config_code + merged_content[header_end+17:]

# Write the final merged mod
with open('/workspace/FINAL_WORKING_MERGE.js', 'w') as f:
    f.write(merged_content)

print("\nSUCCESS: Created FINAL_WORKING_MERGE.js")
print(f"Total size: {len(merged_content)} characters")
