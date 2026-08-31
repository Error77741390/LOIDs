#!/usr/bin/env python3

with open('/workspace/FINAL_WORKING_MERGED.txt', 'r') as f:
    content = f.read()

# Fix remaining configs references in injectStyles
content = content.replace('(configs.pinkUI ? \"#ff9cfb\" : \"#50afef\")', '(globalThis.remedyConfigs.pinkUI ? \"#ff9cfb\" : \"#50afef\")')
content = content.replace('(configs.pinkUI ? \"rgb(93 0 131 / 40%)\" : \"rgba(0, 0, 0, 0.7)\")', '(globalThis.remedyConfigs.pinkUI ? \"rgb(93 0 131 / 40%)\" : \"rgba(0, 0, 0, 0.7)\")')

with open('/workspace/FINAL_WORKING_MERGED.txt', 'w') as f:
    f.write(content)

print("Fix 2 applied!")
