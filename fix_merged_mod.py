#!/usr/bin/env python3

# Read both files
with open('/workspace/Main mod.txt', 'r') as f:
    main_mod = f.read()

with open('/workspace/Remendy mod.txt', 'r') as f:
    remendy_mod = f.read()

# Extract key components from Remendy that are needed

# 1. Extract getEl function (around line 411)
getEl_code = """
globalThis.getEl = function(id) {
    return document.getElementById(id) || [];
}
"""

# 2. Extract HtmlAction and Html classes (lines 3341-3532)
import re

# Find HtmlAction class
htmlaction_match = re.search(r'(class HtmlAction \{.*?)(?=class Html \{)', remendy_mod, re.DOTALL)
htmlaction_code = htmlaction_match.group(1) if htmlaction_match else ""

# Find Html class  
html_match = re.search(r'(class Html \{.*?)(?=globalThis\.validID|globalThis\.menuDiv)', remendy_mod, re.DOTALL)
html_code = html_match.group(1) if html_match else ""

# 3. Extract menuDiv creation and HTML initialization
menuDiv_match = re.search(r'(globalThis\.menuDiv = document\.createElement.*?)(?=HTML\.set\("menuDiv"\))', remendy_mod, re.DOTALL)
menuDiv_code = menuDiv_match.group(1) if menuDiv_match else ""

# 4. Extract HTML.set and initial styles
html_set_match = re.search(r'(HTML\.set\("menuDiv"\);.*?)(?=getEl\("nameInput"\))', remendy_mod, re.DOTALL)
html_set_code = html_set_match.group(1) if html_set_match else ""

# 5. Extract menuChatDiv setup
menuChat_match = re.search(r'(globalThis\.menuChatDiv = document\.createElement.*?globalThis\.menuCBFocus = false;)', remendy_mod, re.DOTALL)
menuChat_code = menuChat_match.group(1) if menuChat_match else ""

# 6. Extract configs object with visual settings only
configs_match = re.search(r'(globalThis\.configs = JSON\.parse\(localStorage\.getItem\("remedyConfig"\)\) \|\| \{[^}]+\};)', remendy_mod, re.DOTALL)

# Build the complete config with just visual/customization settings
visual_configs = """
globalThis.configs = {
    menuOpacity: 0.7,
    menuColor: "#000000b7",
    mainColor: "rgba(0, 0, 0, 0.7)",
    textColor: "#e0e0e0",
    toggleColor: "#494b48",
    outlineColor: "#e0e0e0",
    accentColor: "#50afef",
    elementOpacity: 0.1,
    themeColor: "#0c0132",
    grayVis: false,
    bigNames: false,
    showGrid: true,
    borders: false,
    nightMode: false,
    darkMode: false,
    pinkUI: false,
    bowTie: false,
    texturePack: "none"
};
"""

# 7. Extract injectStyles function
injectStyles_match = re.search(r'(globalThis\.injectStyles = function\(\) \{.*?\n\};)', remendy_mod, re.DOTALL)
injectStyles_code = injectStyles_match.group(1) if injectStyles_match else ""

# 8. Extract toggleMenuChat function
toggleMenu_match = re.search(r'(globalThis\.toggleMenuChat = function\(\) \{.*?\n\})', remendy_mod, re.DOTALL)
toggleMenu_code = toggleMenu_match.group(1) if toggleMenu_match else ""

print("Extracted components:")
print(f"getEl: {len(getEl_code)} chars")
print(f"HtmlAction: {len(htmlaction_code)} chars")
print(f"Html: {len(html_code)} chars")
print(f"menuDiv: {len(menuDiv_code)} chars")
print(f"HTML.set: {len(html_set_code)} chars")
print(f"menuChat: {len(menuChat_code)} chars")
print(f"injectStyles: {len(injectStyles_code)} chars")
print(f"toggleMenu: {len(toggleMenu_code)} chars")

# Now let's find where to insert these in the main mod
# We'll insert after the settings object and before the first major function

# Find the end of settings object in main mod
settings_end = main_mod.find('let settings = {')
if settings_end == -1:
    # Try alternate pattern
    settings_end = main_mod.find('// MERGED SETTINGS')
    
# Find a good insertion point - after initial variable declarations but before major functions
insertion_point = main_mod.find('// X- precision tuning:')
if insertion_point == -1:
    insertion_point = main_mod.find('const X_PRECISION = {')

print(f"\nInsertion point at: {insertion_point}")

# Create the merged content
merged_parts = []

# Part 1: Header and initial variables from main mod
header_end = main_mod.find('let settings = {')
if header_end == -1:
    header_end = insertion_point

part1 = main_mod[:header_end]

# Part 2: Settings from main mod (keep original)
settings_start = main_mod.find('let settings = {')
settings_end_marker = main_mod.find('};', settings_start)
if settings_end_marker != -1:
    settings_block = main_mod[settings_start:settings_end_marker + 2]
else:
    settings_block = ""

# Part 3: Add Remendy components
remendy_components = f"""
{getEl_code}

{htmlaction_code}

{html_code}

{menuDiv_code}

{html_set_code}

{menuChat_code}

{visual_configs}

{injectStyles_code}

{toggleMenu_code}
"""

# Part 4: Rest of main mod (from X_PRECISION onwards)
rest_of_main = main_mod[insertion_point:]

# Combine everything
final_content = part1 + settings_block + "\n\n// === REMENDY VISUAL COMPONENTS ===\n" + remendy_components + "\n// === END REMENDY VISUAL COMPONENTS ===\n\n" + rest_of_main

# Write the fixed merged mod
with open('/workspace/Merged_Complete_Mod_FIXED.txt', 'w') as f:
    f.write(final_content)

print(f"\n✅ Created fixed merged mod: {len(final_content)} characters")
print(f"Original main mod: {len(main_mod)} characters")
print(f"Remendy mod: {len(remendy_mod)} characters")

