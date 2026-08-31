#!/usr/bin/env python3
import re

# Read both files
with open("/workspace/Remendy mod.txt", "r", encoding="utf-8") as f:
    remendy_code = f.read()

with open("/workspace/Main mod.txt", "r", encoding="utf-8") as f:
    main_code = f.read()

# Extract the hatFc function from Main mod (lines ~15156-15308)
hat_function_match = re.search(r'(function hatFc\(\) \{.*?)(?=\n\s*\/\/ FIND OBJECTS BY ID\/SID:|\n\s*function findPlayerByID)', main_code, re.DOTALL)

if not hat_function_match:
    # Try alternative pattern
    hat_start = main_code.find('function hatFc()')
    if hat_start == -1:
        print("ERROR: Could not find hatFc function in Main mod")
        exit(1)
    
    # Find the end by looking for the next major function
    next_function_patterns = [
        '\n            // FIND OBJECTS BY ID/SID:',
        '\n            function findPlayerByID',
        '\n        function findPlayerByID',
        '\n    function findPlayerByID'
    ]
    
    hat_end = len(main_code)
    for pattern in next_function_patterns:
        pos = main_code.find(pattern, hat_start + 50)
        if pos != -1 and pos < hat_end:
            hat_end = pos
    
    hat_function_code = main_code[hat_start:hat_end]
else:
    hat_function_code = hat_function_match.group(1)

print(f"Extracted hat function length: {len(hat_function_code)} chars")

# Now we need to find where in Remendy to insert/replace hat logic
# Remendy uses hatSwitcher function, we need to either:
# 1. Replace hatSwitcher with hatFc
# 2. Or modify hatSwitcher to use Main mod's logic

# Let's find the hatSwitcher function in Remendy
hat_switcher_start = remendy_code.find('globalThis.hatSwitcher = function(returnHat)')
if hat_switcher_start == -1:
    print("ERROR: Could not find hatSwitcher in Remendy")
    exit(1)

# Find where hatSwitcher is called in Remendy
hat_call_pattern = r'const equipHat = hatSwitcher\(true\);|hatSwitcher\(true\)|hatSwitcher\(\)'
hat_calls = list(re.finditer(hat_call_pattern, remendy_code))
print(f"Found {len(hat_calls)} calls to hatSwitcher")

# Strategy: We'll keep Remendy's structure but replace the hatSwitcher function body
# with a wrapper that calls Main mod's hatFc logic

# First, let's create a modified version that:
# 1. Keeps Remendy's header and structure
# 2. Adds Main mod's hat-related variables (currentHat, etc.)
# 3. Replaces hatSwitcher with a function that uses Main mod's hatFc logic

# Find where configs ends in Remendy
configs_end = remendy_code.find('};', remendy_code.find('globalThis.configs = JSON.parse'))
if configs_end == -1:
    print("ERROR: Could not find configs end")
    exit(1)

# Insert currentHat variable after configs
insert_point = configs_end + 2  # After };

# Create the insertion code
insertion_code = '''

// === MAIN MOD HAT VARIABLES ===
let currentHat = 0;
let currentAcc = 0;

// Helper function to check if hat is bought (from Main mod)
function isBoughtHat(id, type) {
    if (!player) return false;
    if (type === 0) {
        return player.skins && player.skins[id];
    } else if (type === 1) {
        return player.tails && player.tails[id];
    }
    return false;
}

'''

# Now modify remendy_code to add our variables
modified_remedy = remendy_code[:insert_point] + insertion_code + remendy_code[insert_point:]

# Now we need to replace the hatSwitcher function
# Find the start of hatSwitcher (there are two versions - one for dev server, one for normal)
hat_switcher_matches = list(re.finditer(r'globalThis\.hatSwitcher = function\(returnHat\) \{', modified_remedy))
print(f"Found {len(hat_switcher_matches)} hatSwitcher definitions")

if len(hat_switcher_matches) >= 2:
    # Get the second one (non-dev server version)
    second_hat_start = hat_switcher_matches[1].start()
    
    # Find where this function ends (look for the closing brace at same indentation)
    # This is tricky, so we'll look for the next major section
    next_sections = [
        '\nif (!spyBot) clearChat();',
        '\nasync function receiveChat',
        '\nwindow.changeMenu',
        '\n// MENU FUNCTIONS:'
    ]
    
    hat_end_pos = len(modified_remedy)
    for section in next_sections:
        pos = modified_remedy.find(section, second_hat_start + 100)
        if pos != -1 and pos < hat_end_pos:
            hat_end_pos = pos
    
    # Create replacement hatSwitcher that uses Main mod logic
    new_hat_switcher = '''
// === MAIN MOD HAT LOGIC INTEGRATED ===
globalThis.hatSwitcher = function(returnHat) {
    // Call Main mod's hat logic
    try {
        hatFc();
        
        // Return the current hat if requested
        if (returnHat) {
            return currentHat;
        }
        
        // The hat() and acc() functions are called inside hatFc
        return null;
    } catch (e) {
        console.log("Hat switcher error:", e);
        return null;
    }
}

'''
    
    # Replace the second hatSwitcher onwards
    final_code = modified_remedy[:second_hat_start] + new_hat_switcher + modified_remedy[hat_end_pos:]
else:
    # If only one hatSwitcher, just append our version at the end before the game loop
    # Find a good insertion point
    game_loop_start = final_code.find('function gameLoop')
    if game_loop_start == -1:
        game_loop_start = final_code.find('requestAnimationFrame')
    
    if game_loop_start != -1:
        final_code = modified_remedy[:game_loop_start] + new_hat_switcher + modified_remedy[game_loop_start:]
    else:
        final_code = modified_remedy + new_hat_switcher

# Write the result
with open("/workspace/FINAL_MERGED_HAT_MOD.txt", "w", encoding="utf-8") as f:
    f.write(final_code)

print(f"Created FINAL_MERGED_HAT_MOD.txt ({len(final_code)} chars)")
print("Done!")
