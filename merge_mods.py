#!/usr/bin/env python3
"""
Merge Remendy visual customization into Main mod
- Keep all Main mod combat/placement logic
- Add Remendy's visual settings and UI customization
- Fix FPS flickering with Remendy's smoother render loop
- EXCLUDE: auto placer, healing, hat automation from Remendy
"""

import re

# Read files
with open('/workspace/Main mod.txt', 'r', encoding='utf-8') as f:
    main_mod = f.read()

with open('/workspace/Remendy mod.txt', 'r', encoding='utf-8') as f:
    remendy_mod = f.read()

# Extract injectStyles function
inject_styles_start = remendy_mod.find('globalThis.injectStyles = function() {')
inject_styles_end = remendy_mod.find('globalThis.injectScrollbarStyles', inject_styles_start)
inject_styles_func = remendy_mod[inject_styles_start:inject_styles_end].strip()

# Extract toggleMenuChat function  
toggle_menu_start = remendy_mod.find('globalThis.toggleMenuChat = function()')
brace_count = 0
toggle_menu_end = toggle_menu_start
for i, char in enumerate(remendy_mod[toggle_menu_start:], toggle_menu_start):
    if char == '{':
        brace_count += 1
    elif char == '}':
        brace_count -= 1
        if brace_count == 0:
            toggle_menu_end = i + 1
            break
toggle_menu_func = remendy_mod[toggle_menu_start:toggle_menu_end]

# Extract configs object
configs_start = remendy_mod.find('globalThis.configs = JSON.parse(localStorage.getItem("remedyConfig")) || {')
configs_lines = []
brace_count = 0
in_configs = False
for i, line in enumerate(remendy_mod[configs_start:].split('\n'), 0):
    if not in_configs and 'globalThis.configs = JSON.parse' in line:
        in_configs = True
        brace_count = 1
        configs_lines.append(line)
    elif in_configs:
        configs_lines.append(line)
        brace_count += line.count('{') - line.count('}')
        if brace_count <= 0:
            break
configs_full = '\n'.join(configs_lines)

# Build merged settings (Main mod settings + Remendy visual configs)
merged_settings = """// MERGED SETTINGS - Main mod core + Remendy visual customization
let settings = {
    botplatformplacer: false,
    botcount: 40,
    botname: "Helper",
    gamezoom: 100,
    x18ksync: true,
    chatlog: false,
    spampreplace: true,
    autoPlace: true,

    // PERFORMANCE SETTINGS
    uncapFPS: true,
    showFPS: true,
    lowPacketMode: false,

    // COMBAT SETTINGS
    instaKey: 'r',
    instaEnabled: false,
    instaThreshold: 35,

    // MOVEMENT SETTINGS
    smartMovement: true,
    spikeAvoidance: true,
    playerAvoidance: true,
    avoidDistance: 150,

    // PLACER SETTINGS
    angleOptimize: true,
    anglePrecision: 2.5,

    // REMENDY VISUAL CUSTOMIZATION SETTINGS (MERGED)
    grayVis: true,
    bigNames: false,
    showGrid: true,
    borders: true,
    nightMode: true,
    darkMode: true,
    pinkUI: false,
    bowTie: false,
    texturePack: false,
    
    // COLOR CUSTOMIZATION (from Remendy)
    menuOpacity: 0.9,
    menuColor: "#01000580",
    mainColor: "#000105b3",
    textColor: "#e8e8e8",
    toggleColor: "#006fe6",
    outlineColor: "#d6d6d6",
    accentColor: "#fef1f1",
    elementOpacity: 0.1,
    themeColor: "#0c0132",
};"""

# Find where to insert the merged settings in Main mod (replace original settings block)
settings_pattern = r'let settings = \{[^}]+\};'
main_mod_new = re.sub(settings_pattern, merged_settings, main_mod, count=1, flags=re.DOTALL)

# Find the doUpdate function and replace setTimeout with requestAnimationFrame for smoother FPS
old_update_pattern = r"setTimeout\(\(\) => requestAnimationFrame\(doUpdate\), 16\.67\);"
new_update_code = """// Use Remendy-style smooth render loop
window.requestAnimationFrame(doUpdate);"""
main_mod_new = re.sub(old_update_pattern, new_update_code, main_mod_new)

# Find a good place to inject the Remendy functions (before webpack bootstrap or after globals)
# Insert after the global variables section
insert_marker = "let packetQueue = [];"
insert_pos = main_mod_new.find(insert_marker)
if insert_pos != -1:
    insert_pos = main_mod_new.find('\n', insert_pos + len(insert_marker))
    injection_code = f"""
// ===== REMENDY VISUAL CUSTOMIZATION (MERGED) =====
{configs_full}

{inject_styles_func}

{toggle_menu_func}

// ===== END REMENDY VISUAL CUSTOMIZATION =====
"""
    main_mod_new = main_mod_new[:insert_pos] + injection_code + main_mod_new[insert_pos:]

# Write the merged mod
with open('/workspace/Merged_Complete_Mod.txt', 'w', encoding='utf-8') as f:
    f.write(main_mod_new)

print(f"Merged mod created successfully!")
print(f"Total length: {len(main_mod_new)} characters")
print(f"Added injectStyles: {len(inject_styles_func)} chars")
print(f"Added toggleMenuChat: {len(toggle_menu_func)} chars")
print(f"Added configs: {len(configs_full)} chars")
