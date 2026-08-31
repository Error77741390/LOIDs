#!/usr/bin/env python3
import re

# Read both files
with open('/workspace/Main mod.txt', 'r') as f:
    main_mod = f.read()

with open('/workspace/Remendy mod.txt', 'r') as f:
    remendy_mod = f.read()

# Extract Remendy components we need:

# 1. Extract configs object (lines 3119 to around 3280)
configs_match = re.search(r'(globalThis\.configs = JSON\.parse\(localStorage\.getItem\("remedyConfig"\)\) \| \{[^}]+\};)', remendy_mod, re.DOTALL)
if not configs_match:
    # Try a different pattern for the configs
    configs_start = remendy_mod.find('globalThis.configs = JSON.parse(localStorage.getItem("remedyConfig"))')
    if configs_start != -1:
        # Find the end of the configs object by counting braces
        brace_count = 0
        start_brace = remendy_mod.find('{', configs_start)
        for i in range(start_brace, len(remendy_mod)):
            if remendy_mod[i] == '{':
                brace_count += 1
            elif remendy_mod[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    configs_content = remendy_mod[configs_start:i+1]
                    break
    else:
        configs_content = ""
else:
    configs_content = configs_match.group(1)

# 2. Extract getEl function
getEl_match = re.search(r'(globalThis\.getEl = function\(id\) \{[^}]+\})', remendy_mod)
getEl_func = getEl_match.group(1) if getEl_match else ""

# 3. Extract HtmlAction class
htmlAction_start = remendy_mod.find('class HtmlAction {')
if htmlAction_start != -1:
    brace_count = 0
    start_brace = remendy_mod.find('{', htmlAction_start)
    for i in range(start_brace, len(remendy_mod)):
        if remendy_mod[i] == '{':
            brace_count += 1
        elif remendy_mod[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                htmlAction_class = remendy_mod[htmlAction_start:i+1]
                break
else:
    htmlAction_class = ""

# 4. Extract Html class
html_start = remendy_mod.find('class Html {')
if html_start != -1:
    brace_count = 0
    start_brace = remendy_mod.find('{', html_start)
    for i in range(start_brace, len(remendy_mod)):
        if remendy_mod[i] == '{':
            brace_count += 1
        elif remendy_mod[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                html_class = remendy_mod[html_start:i+1]
                break
else:
    html_class = ""

# 5. Extract menuDiv creation
menuDiv_match = re.search(r'(globalThis\.menuDiv = document\.createElement\("div"\);[^;]+;)', remendy_mod)
menuDiv_code = menuDiv_match.group(1) if menuDiv_match else ""

# 6. Extract menuChatDiv creation  
menuChatDiv_match = re.search(r'(globalThis\.menuChatDiv = document\.createElement\("div"\);[^;]+;)', remendy_mod)
menuChatDiv_code = menuChatDiv_match.group(1) if menuChatDiv_match else ""

# 7. Extract toggleMenuChat function
toggleMatch = re.search(r'(globalThis\.toggleMenuChat = function\(\) \{[^}]+\})', remendy_mod)
toggleMenuChat_func = toggleMatch.group(1) if toggleMatch else ""

# 8. Extract injectStyles function
inject_start = remendy_mod.find('globalThis.injectStyles = function() {')
if inject_start != -1:
    brace_count = 0
    start_brace = remendy_mod.find('{', inject_start)
    for i in range(start_brace, len(remendy_mod)):
        if remendy_mod[i] == '{':
            brace_count += 1
        elif remendy_mod[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                injectStyles_func = remendy_mod[inject_start:i+1]
                break
else:
    injectStyles_func = ""

# Create the merged content
# Find where to insert the Remendy components in Main mod - after the settings object
settings_end = main_mod.find('let settings = {')
if settings_end != -1:
    # Find the end of settings object
    brace_count = 0
    start_brace = main_mod.find('{', settings_end)
    for i in range(start_brace, len(main_mod)):
        if main_mod[i] == '{':
            brace_count += 1
        elif main_mod[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                settings_end_pos = i + 1
                break
    
    # Insert Remendy components after settings
    remendy_components = f'''
// ========== REMENDY VISUAL CUSTOMIZATION (MERGED) ==========
{getEl_func}

{configs_content.replace('globalThis.configs', 'globalThis.remedyConfigs')}

{htmlAction_class}

{html_class}

globalThis.HTML = new Html();

{menuDiv_code.replace('globalThis.menuDiv', 'globalThis.menuDiv')}
HTML.set("menuDiv");

{menuChatDiv_code.replace('globalThis.menuChatDiv', 'globalThis.menuChatDiv')}
HTML.set("menuChatDiv");

globalThis.menuChatBox = getEl("mChBox");

{toggleMenuChat_func.replace('globalThis.toggleMenuChat', 'globalThis.toggleMenuChat')}

{injectStyles_func.replace('globalThis.injectStyles', 'globalThis.injectStyles')}

// Apply styles on load
if (typeof globalThis.injectStyles === 'function') {{
    globalThis.injectStyles();
}}
// ===========================================================

'''
    merged_mod = main_mod[:settings_end_pos] + remendy_components + main_mod[settings_end_pos:]
else:
    merged_mod = main_mod

# Fix the flickering issue
merged_mod = merged_mod.replace('setTimeout(() => requestAnimationFrame(doUpdate), 16.67);', 'requestAnimationFrame(doUpdate);')

# Write the merged file
with open('/workspace/FINAL_WORKING_MERGED.txt', 'w') as f:
    f.write(merged_mod)

print("Merge complete!")
print(f"Original Main mod size: {len(main_mod)} chars")
print(f"Merged mod size: {len(merged_mod)} chars")
