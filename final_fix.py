#!/usr/bin/env python3

# Read the file
with open("/workspace/FINAL_COMPLETE_REMEDY_MAIN_HAT.txt", "r", encoding="utf-8") as f:
    code = f.read()

# Find where hatSwitcher is called in the game loop
# In Remendy, it's typically called in the main update section
# Let's search for patterns around line 14233 from original Remendy

# Search for where hat logic executes in game loop
search_patterns = [
    'const predictedHat = hatSwitcher(true)',
    'predictedHat = hatSwitcher',
    'hatSwitcher(true)',
    'hatSwitcher(false)',
]

found_pos = -1
for pattern in search_patterns:
    pos = code.find(pattern)
    if pos != -1:
        found_pos = pos
        print(f"Found pattern '{pattern}' at position {pos}")
        break

if found_pos == -1:
    # Try to find where we should insert the update call
    # Look for the Main() function call at the end
    main_call = code.find('Main();')
    if main_call != -1:
        # Insert our update function definition before Main()
        insert_pos = code.rfind('\n', 0, main_call)
        
        update_function = '''
// === HAT VARIABLES UPDATE FUNCTION ===
function updateHatVariables() {
    if (typeof player !== 'undefined' && player) {
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
        
        // Sync reload arrays
        if (player.primaryReload !== undefined) primaryReload[player.sid] = player.primaryReload;
        if (player.secondaryReload !== undefined) secondaryReload[player.sid] = player.secondaryReload;
        if (player.turretReload !== undefined) turretReload[player.sid] = player.turretReload;
        
        // Sync other vars
        predictWeapon = player.weaponIndex || 0;
        autogathering = player.autoGathering || false;
        soldierAnti = player.soldierAnti || false;
        imTrapped = player.imTrapped || false;
        spikeTickAnti = player.spikeTickAnti || false;
        shouldResetShame = player.shouldResetShame || false;
        
        // Sync insta
        if (player.primary) insta.primary = true;
        if (player.secondary) insta.secondary = true;
    }
}

// Call updateHatVariables periodically
setInterval(updateHatVariables, 50);

'''
        
        modified_code = code[:insert_pos] + update_function + code[insert_pos:]
        
        with open("/workspace/FINAL_READY_TO_USE_MOD.txt", "w", encoding="utf-8") as f:
            f.write(modified_code)
        
        print(f"Created FINAL_READY_TO_USE_MOD.txt ({len(modified_code)} chars)")
    else:
        print("ERROR: Could not find insertion point")
        exit(1)
else:
    # Insert update function before the hatSwitcher call
    line_start = code.rfind('\n', 0, found_pos) + 1
    
    update_function = '''
// === HAT VARIABLES UPDATE FUNCTION ===
function updateHatVariables() {
    if (typeof player !== 'undefined' && player) {
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
        
        // Sync reload arrays
        if (player.primaryReload !== undefined) primaryReload[player.sid] = player.primaryReload;
        if (player.secondaryReload !== undefined) secondaryReload[player.sid] = player.secondaryReload;
        if (player.turretReload !== undefined) turretReload[player.sid] = player.turretReload;
        
        // Sync other vars
        predictWeapon = player.weaponIndex || 0;
        autogathering = player.autoGathering || false;
        soldierAnti = player.soldierAnti || false;
        imTrapped = player.imTrapped || false;
        spikeTickAnti = player.spikeTickAnti || false;
        shouldResetShame = player.shouldResetShame || false;
        
        // Sync insta
        if (player.primary) insta.primary = true;
        if (player.secondary) insta.secondary = true;
    }
}

updateHatVariables();

'''
    
    modified_code = code[:line_start] + update_function + code[line_start:]
    
    with open("/workspace/FINAL_READY_TO_USE_MOD.txt", "w", encoding="utf-8") as f:
        f.write(modified_code)
    
    print(f"Created FINAL_READY_TO_USE_MOD.txt ({len(modified_code)} chars)")

print("Done!")
