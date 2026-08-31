#!/usr/bin/env python3

# Read the fixed mod
with open('/workspace/Merged_Complete_Mod_FIXED.txt', 'r') as f:
    content = f.read()

# Fix the FPS flickering issue by replacing setTimeout + requestAnimationFrame with pure requestAnimationFrame
old_code = "setTimeout(() => requestAnimationFrame(doUpdate), 16.67);"
new_code = "requestAnimationFrame(doUpdate);"

content = content.replace(old_code, new_code)

# Write the final version
with open('/workspace/FINAL_MERGED_MOD.txt', 'w') as f:
    f.write(content)

print("✅ Fixed FPS flickering issue!")
print(f"Created FINAL_MERGED_MOD.txt with {len(content)} characters")

