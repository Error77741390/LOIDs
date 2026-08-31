#!/usr/bin/env python3

# Read the current merged file
with open("/workspace/FINAL_MERGED_HAT_MOD.txt", "r", encoding="utf-8") as f:
    merged_code = f.read()

# Read Main mod to extract hatFc function
with open("/workspace/Main mod.txt", "r", encoding="utf-8") as f:
    main_code = f.read()

# Extract hatFc function from Main mod
hat_start = main_code.find('function hatFc()')
if hat_start == -1:
    print("ERROR: Could not find hatFc in Main mod")
    exit(1)

# Find end of hatFc function - look for next major section
next_section_markers = [
    '\n            // FIND OBJECTS BY ID/SID:',
    '\n            function findPlayerByID',
    '\n        // FIND OBJECTS',
    '\n        function find'
]

hat_end = len(main_code)
for marker in next_section_markers:
    pos = main_code.find(marker, hat_start + 100)
    if pos != -1 and pos < hat_end:
        hat_end = pos

hat_fc_function = main_code[hat_start:hat_end]
print(f"Extracted hatFc function: {len(hat_fc_function)} chars")

# Also extract isBoughtHat function if it exists separately
isBoughtHat_start = main_code.find('function isBoughtHat(')
if isBoughtHat_start == -1:
    # Try inline version
    isBoughtHat_start = main_code.find('isBoughtHat = ')

# Find where to insert hatFc in merged code - after configs and helper functions
# Insert before hatSwitcher
hatSwitcher_pos = merged_code.find('// === MAIN MOD HAT LOGIC INTEGRATED ===')
if hatSwitcher_pos == -1:
    hatSwitcher_pos = merged_code.find('globalThis.hatSwitcher = function(returnHat)')

if hatSwitcher_pos == -1:
    print("ERROR: Could not find insertion point")
    exit(1)

# Insert hatFc function before hatSwitcher
insertion_text = '''
// === MAIN MOD HAT FUNCTION ===
''' + hat_fc_function + '''
// === END HAT FUNCTION ===

'''

# Insert the function
final_code = merged_code[:hatSwitcher_pos] + insertion_text + merged_code[hatSwitcher_pos:]

# Write result
with open("/workspace/COMPLETE_HAT_MERGED_MOD.txt", "w", encoding="utf-8") as f:
    f.write(final_code)

print(f"Created COMPLETE_HAT_MERGED_MOD.txt ({len(final_code)} chars)")
print("Done!")
