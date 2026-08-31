#!/usr/bin/env python3
import re

# Read both files
with open("/workspace/Main mod.txt", "r") as f:
    main_mod = f.read()

with open("/workspace/Remendy mod.txt", "r") as f:
    remendy_mod = f.read()

# Extract Remendy components we need:

# 1. Extract configs (lines 3119 to ~3275)
configs_match = re.search(r'(globalThis\.configs = JSON\.parse\(localStorage\.getItem\("remedyConfig"\)\) \|\| \{[^}]+\};)', remendy_mod, re.DOTALL)
if not configs_match:
    # Try to find the full configs block more carefully
    start_idx = remendy_mod.find('globalThis.configs = JSON.parse(localStorage.getItem("remedyConfig")) || {')
    if start_idx != -1:
        brace_count = 0
        end_idx = start_idx
        for i, char in enumerate(remendy_mod[start_idx:], start_idx):
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_idx = i + 1
                    break
        configs_block = remendy_mod[start_idx:end_idx]
    else:
        configs_block = ""
else:
    configs_block = configs_match.group(1)

# 2. Extract getEl function
getEl_match = re.search(r'(globalThis\.getEl = function\(id\) \{[^}]+\})', remendy_mod)
getEl_func = getEl_match.group(1) if getEl_match else ""

# 3. Extract HtmlAction and Html classes
htmlAction_start = remendy_mod.find('class HtmlAction {')
html_class_start = remendy_mod.find('class Html {')
html_instance = remendy_mod.find('globalThis.HTML = new Html();')

if htmlAction_start != -1 and html_instance != -1:
    # Find end of HTML instance line
    html_instance_end = remendy_mod.find('\n', html_instance)
    if html_instance_end == -1:
        html_instance_end = len(remendy_mod)
    else:
        html_instance_end += 1
    html_classes_block = remendy_mod[htmlAction_start:html_instance_end]
else:
    html_classes_block = ""

# 4. Extract menuDiv creation
menuDiv_start = remendy_mod.find('globalThis.menuDiv = document.createElement("div");')
menuChat_start = remendy_mod.find('globalThis.menuChatDiv = document.createElement("div");')
menuChat_end_marker = remendy_mod.find('window.clearChat = function ()', menuChat_start)
if menuChat_end_marker == -1:
    menuChat_end_marker = remendy_mod.find('\n', menuChat_start + 2000)
else:
    # Go back to before this function
    pass

if menuDiv_start != -1 and menuChat_start != -1:
    menu_system_block = remendy_mod[menuDiv_start:menuChat_start + 2500]  # Approximate end
else:
    menu_system_block = ""

# 5. Extract injectStyles function
injectStyles_start = remendy_mod.find('globalThis.injectStyles = function() {')
if injectStyles_start != -1:
    brace_count = 0
    end_idx = injectStyles_start
    for i, char in enumerate(remendy_mod[injectStyles_start:], injectStyles_start):
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                end_idx = i + 1
                break
    injectStyles_block = remendy_mod[injectStyles_start:end_idx]
else:
    injectStyles_block = ""

# 6. Extract toggleMenuChat function
toggleMenu_start = remendy_mod.find('globalThis.toggleMenuChat = function() {')
if toggleMenu_start != -1:
    brace_count = 0
    end_idx = toggleMenu_start
    for i, char in enumerate(remendy_mod[toggleMenu_start:], toggleMenu_start):
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                end_idx = i + 1
                break
    toggleMenu_block = remendy_mod[toggleMenu_start:end_idx]
else:
    toggleMenu_block = ""

# Now build the merged mod:
# Start with Main mod header
merged = main_mod

# Find where to insert the Remendy UI code - after settings but before webpack
# Look for the settings block end and webpack start
settings_end = main_mod.find('const autoBuyList = [')
webpack_start = main_mod.find('/******/ (function (modules) { // webpackBootstrap')

if settings_end != -1 and webpack_start != -1:
    # Insert Remendy UI components here
    ui_code = f'''
// ============================================
// REMENDY VISUAL CUSTOMIZATION SYSTEM (MERGED)
// ============================================

{getEl_func}

{configs_block.replace('globalThis.configs', 'globalThis.configs')}

{html_classes_block}

{menu_system_block}

{injectStyles_block}

{toggleMenu_block}

// Initialize styles on load
try {{
    if (typeof globalThis.injectStyles === 'function') {{
        globalThis.injectStyles();
    }}
}} catch(e) {{ console.log("Style injection pending"); }}

'''
    
    merged = main_mod[:settings_end] + ui_code + main_mod[settings_end:]

# Fix the flickering issue - replace setTimeout requestAnimationFrame pattern
# Find the doUpdate or render loop and fix it
old_pattern = r'setTimeout\(\(\) => requestAnimationFrame\((doUpdate|render|updateGame)\),\s*16\.67\)'
new_pattern = r'window.requestAnimationFrame(\1)'

merged = re.sub(old_pattern, new_pattern, merged)

# Also try simpler pattern
merged = re.sub(r'setTimeout\(\(\) => requestAnimationFrame\(doUpdate\), 16\.67\)', 'window.requestAnimationFrame(doUpdate)', merged)

# Write the merged file
with open("/workspace/FINAL_COMPLETE_MERGED.txt", "w") as f:
    f.write(merged)

print(f"Merged mod created successfully!")
print(f"Configs block length: {len(configs_block)}")
print(f"getEl function length: {len(getEl_func)}")
print(f"HTML classes length: {len(html_classes_block)}")
print(f"Menu system length: {len(menu_system_block)}")
print(f"injectStyles length: {len(injectStyles_block)}")
print(f"toggleMenuChat length: {len(toggleMenu_block)}")
