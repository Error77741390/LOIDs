#!/usr/bin/env python3

# Read the file
with open("/workspace/FINAL_REMENDY_WITH_MAIN_HAT.txt", "r", encoding="utf-8") as f:
    code = f.read()

# The hatFc function uses myPlayer but Remendy uses player
# We need to update hatFc to use player instead of myPlayer

# Replace myPlayer with player in hatFc function only
hat_fc_start = code.find('function hatFc()')
if hat_fc_start == -1:
    print("ERROR: Could not find hatFc")
    exit(1)

# Find end of hatFc
hat_fc_end_marker = code.find('// === END HAT FUNCTION ===', hat_fc_start)
if hat_fc_end_marker == -1:
    print("ERROR: Could not find end of hatFc")
    exit(1)

hat_fc_end = hat_fc_end_marker

# Split the code
before_hat = code[:hat_fc_start]
hat_function = code[hat_fc_start:hat_fc_end]
after_hat = code[hat_fc_end:]

# Replace myPlayer with player in hat function only
# But keep currentAcc declaration
modified_hat = hat_function.replace('myPlayer.x2', 'player.x2')
modified_hat = modified_hat.replace('myPlayer.y2', 'player.y2')
modified_hat = modified_hat.replace('myPlayer.weapons', 'player.weapons')
modified_hat = modified_hat.replace('myPlayer.sid', 'player.sid')
modified_hat = modified_hat.replace('myPlayer.skinIndex', 'player.skinIndex')
modified_hat = modified_hat.replace('myPlayer.xVel', 'player.xVel')
modified_hat = modified_hat.replace('myPlayer.yVel', 'player.yVel')
modified_hat = modified_hat.replace('myPlayer.primary', 'player.primary')
modified_hat = modified_hat.replace('myPlayer.skins', 'player.skins')
modified_hat = modified_hat.replace('myPlayer.tails', 'player.tails')

# Also update the variables section to use player
code_with_vars = before_hat + modified_hat + after_hat

# Write result
with open("/workspace/REMEDY_WITH_MAIN_HAT_FINAL.txt", "w", encoding="utf-8") as f:
    f.write(code_with_vars)

print(f"Created REMEDY_WITH_MAIN_HAT_FINAL.txt ({len(code_with_vars)} chars)")
print("Done!")
