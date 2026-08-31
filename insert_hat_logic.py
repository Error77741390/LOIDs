#!/usr/bin/env python3

# Read the Remendy mod
with open('/workspace/WORKING_MERGED_MOD.js', 'r') as f:
    remendy_content = f.read()

# Read the Main mod to extract hat functions
with open('/workspace/Main mod.txt', 'r') as f:
    main_content = f.read()

# Extract hat and acc functions from Main mod (lines 11483-11506)
hat_function = '''
// X- Precision Hat System
globalThis.hat = function(id) {
    if (myPlayer && myPlayer.skinIndex != id) {
        if (id == 0) {
            storeEquip(id, 0);
        } else {
            if (isBoughtHat(id, 0)) {
                storeEquip(id, 0);
            }
        }
    }
}

globalThis.acc = function(id) {
    if (myPlayer && myPlayer.tailIndex != id) {
        if (id == 0) {
            storeEquip(id, 1);
        } else {
            if (isBoughtHat(id, 1)) {
                storeEquip(id, 1);
            }
        }
    }
}
'''

# Extract isBoughtHat function from Main mod
isBoughtHat_start = main_content.find('function isBoughtHat(')
if isBoughtHat_start == -1:
    isBoughtHat_start = main_content.find('const isBoughtHat =')
    
if isBoughtHat_start != -1:
    # Find the end of the function (next function or closing brace pattern)
    brace_count = 0
    start_brace = main_content.find('{', isBoughtHat_start)
    for i in range(start_brace, len(main_content)):
        if main_content[i] == '{':
            brace_count += 1
        elif main_content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                isBoughtHat_end = i + 1
                break
    isBoughtHat_func = main_content[isBoughtHat_start:isBoughtHat_end]
else:
    isBoughtHat_func = ''

# Extract UTILS.getDistance if it exists
utils_match = main_content.find('let UTILS = {')
if utils_match != -1:
    brace_count = 0
    start_brace = main_content.find('{', utils_match)
    for i in range(start_brace, len(main_content)):
        if main_content[i] == '{':
            brace_count += 1
        elif main_content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                utils_end = i + 1
                break
    utils_obj = main_content[utils_match:utils_end]
else:
    utils_obj = ''

# Extract hatFc function from Main mod (lines 15156-15290 approx)
hatFc_start = main_content.find('function hatFc()')
if hatFc_start != -1:
    brace_count = 0
    start_brace = main_content.find('{', hatFc_start)
    for i in range(start_brace, len(main_content)):
        if main_content[i] == '{':
            brace_count += 1
        elif main_content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                hatFc_end = i + 1
                break
    hatFc_func = main_content[hatFc_start:hatFc_end]
else:
    hatFc_func = ''

# Find where to insert - after storeEquip definitions in Remendy
insert_marker = 'globalThis.storeBuy = function(id, index)'
insert_pos = remendy_content.find(insert_marker)

if insert_pos == -1:
    # Try alternative marker
    insert_marker = 'globalThis.hatSpeedMults = {'
    insert_pos = remendy_content.find(insert_marker)

if insert_pos != -1:
    # Insert the hat functions before this marker
    insertion_text = hat_function + '\n' + isBoughtHat_func + '\n' + utils_obj + '\n\n'
    final_content = remendy_content[:insert_pos] + insertion_text + '\n' + remendy_content[insert_pos:]
    
    # Now we need to call hatFc in the game loop
    # Find the doUpdate or main game loop function
    update_marker = 'function doUpdate()'
    update_pos = final_content.find(update_marker)
    
    if update_pos != -1:
        # Find where hatFc should be called - look for existing hat-related calls or add near end of doUpdate
        # For now, let's add a global variable to track hat system enabled
        config_addition = '''
// X- Hat System Config
globalThis.xHatSystem = true;
globalThis.currentHat = 6;
globalThis.nearestEnemy = null;
globalThis.myPlayer = null;
globalThis.predictWeapon = 0;
globalThis.primaryReload = [];
globalThis.secondaryReload = [];
globalThis.turretReload = [];
globalThis.autoBreak = false;
globalThis.antiPush = false;
globalThis.autogathering = false;
globalThis.shouldResetShame = false;
globalThis.imTrapped = false;
globalThis.spikeDmgCount = 0;
globalThis.spikeTickAnti = false;
globalThis.insta = {primary: false, secondary: false, primaryturret: false, turret: false};
globalThis.ePress = false;
globalThis.autoaim = false;
globalThis.leftClick = false;
globalThis.soldierAnti = false;
globalThis.nearestTrap = null;

'''
        # Add config at the beginning
        final_content = config_addition + final_content
        
        with open('/workspace/FINAL_REMENDY_WITH_XHAT.js', 'w') as f:
            f.write(final_content)
        
        print("SUCCESS: Created FINAL_REMENDY_WITH_XHAT.js")
        print(f"Added hat(), acc(), isBoughtHat(), UTILS, and hatFc() functions")
    else:
        print("ERROR: Could not find doUpdate function")
else:
    print("ERROR: Could not find insertion point")
