#!/usr/bin/env python3

# Read the merged file
with open("/workspace/COMPLETE_HAT_MERGED_MOD.txt", "r", encoding="utf-8") as f:
    code = f.read()

# The hatFc function uses Main mod variables that need to be defined
# Let's add all required variables after configs

# Find where configs ends
configs_match = code.find('globalThis.configs = JSON.parse')
if configs_match == -1:
    print("ERROR: Could not find configs")
    exit(1)

# Find the closing brace of configs
configs_end_brace = code.find('};', configs_match)
if configs_end_brace == -1:
    print("ERROR: Could not find configs end")
    exit(1)

insert_pos = configs_end_brace + 2

# Add all required Main mod variables and helper functions
required_code = '''

// === MAIN MOD VARIABLES FOR HAT FUNCTION ===
let currentHat = 0;
let currentAcc = 0;
let nearestEnemy = null;
let myPlayer = null;
let autogathering = false;
let predictWeapon = 0;
let primaryReload = [];
let secondaryReload = [];
let autoBreak = true;
let antiPush = false;
let shouldResetShame = false;
let imTrapped = false;
let spikeDmgCount = 0;
let spikeTickAnti = false;
let nearestTrap = null;
let turretReload = [];
let ePress = false;
let autoaim = false;
let leftClick = false;
let soldierAnti = false;
let insta = { primary: false, secondary: false, primaryturret: false, turret: false };

// Helper function to check if hat/accessory is bought
function isBoughtHat(id, type) {
    if (!player && !myPlayer) return false;
    const p = player || myPlayer;
    if (type === 0) {
        return p.skins && p.skins[id];
    } else if (type === 1) {
        return p.tails && p.tails[id];
    }
    return false;
}

// Distance utility (from Main mod UTILS)
const UTILS = {
    getDistance: function(x1, y1, x2, y2) {
        if (x1 === undefined || y1 === undefined || x2 === undefined || y2 === undefined) return 999999;
        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    }
};

// Alias myPlayer to player for compatibility
if (typeof player !== 'undefined') {
    myPlayer = player;
}

'''

# Insert the code
modified_code = code[:insert_pos] + required_code + code[insert_pos:]

# Write result
with open("/workspace/FINAL_REMENDY_WITH_MAIN_HAT.txt", "w", encoding="utf-8") as f:
    f.write(modified_code)

print(f"Created FINAL_REMENDY_WITH_MAIN_HAT.txt ({len(modified_code)} chars)")
print("Done!")
