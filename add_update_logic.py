#!/usr/bin/env python3

# Read the final file
with open("/workspace/REMEDY_WITH_MAIN_HAT_FINAL.txt", "r", encoding="utf-8") as f:
    code = f.read()

# We need to add code that updates nearestEnemy and other variables in the game loop
# Find where the game update/rendering happens in Remendy

# Look for the main game loop or update function
update_patterns = [
    'function updateGame',
    'function gameLoop',
    'requestAnimationFrame',
    'globalThis.update = function',
]

update_pos = -1
for pattern in update_patterns:
    pos = code.find(pattern)
    if pos != -1 and (update_pos == -1 or pos < update_pos):
        update_pos = pos

if update_pos == -1:
    print("Could not find update function, searching alternatives...")
    # Try finding where player data is processed
    update_pos = code.find('player.x2')
    if update_pos == -1:
        update_pos = len(code) // 2  # Fallback to middle

# Find a good place to insert the variable update logic - after vars are defined but before main loop
# Let's insert it right before hatSwitcher is called

hat_switcher_call = code.find('const equipHat = hatSwitcher(true)')
if hat_switcher_call == -1:
    hat_switcher_call = code.find('hatSwitcher(')

if hat_switcher_call != -1:
    # Insert before the call
    update_code = '''
// === UPDATE MAIN MOD HAT VARIABLES FROM REMENDY PLAYER DATA ===
function updateHatVariables() {
    if (typeof player !== 'undefined' && player) {
        // Update myPlayer alias
        myPlayer = player;
        
        // Find nearest enemy
        nearestEnemy = null;
        let minDist = 999999;
        if (typeof enemy !== 'undefined' && Array.isArray(enemy)) {
            for (let i = 0; i < enemy.length; i++) {
                const e = enemy[i];
                if (!e || !e.x2 || !e.y2) continue;
                const dist = Math.sqrt(Math.pow(e.x2 - player.x2, 2) + Math.pow(e.y2 - player.y2, 2));
                if (dist < minDist) {
                    minDist = dist;
                    nearestEnemy = e;
                }
            }
        }
        
        // Find nearest trap
        nearestTrap = null;
        if (typeof traps !== 'undefined' && traps.in) {
            nearestTrap = traps;
        }
        
        // Sync reload arrays
        if (player.primaryReload !== undefined) primaryReload[player.sid] = player.primaryReload;
        if (player.secondaryReload !== undefined) secondaryReload[player.sid] = player.secondaryReload;
        if (player.turretReload !== undefined) turretReload[player.sid] = player.turretReload;
        
        // Sync weapon info
        predictWeapon = player.weaponIndex || 0;
        
        // Sync flags
        autogathering = player.autoGathering || false;
        shouldResetShame = player.shouldResetShame || false;
        imTrapped = player.imTrapped || false;
        spikeTickAnti = player.spikeTickAnti || false;
        soldierAnti = player.soldierAnti || false;
        
        // Sync insta flags
        insta.primary = player.primary || false;
        insta.secondary = player.secondary || false;
        insta.primaryturret = player.primaryturret || false;
        insta.turret = player.turret || false;
    }
}

// Call updateHatVariables before hat switching
updateHatVariables();

'''
    
    # Find the beginning of the line
    line_start = code.rfind('\n', 0, hat_switcher_call) + 1
    
    modified_code = code[:line_start] + update_code + code[line_start:]
else:
    modified_code = code

# Write result
with open("/workspace/FINAL_COMPLETE_REMEDY_MAIN_HAT.txt", "w", encoding="utf-8") as f:
    f.write(modified_code)

print(f"Created FINAL_COMPLETE_REMEDY_MAIN_HAT.txt ({len(modified_code)} chars)")
print("Done!")
