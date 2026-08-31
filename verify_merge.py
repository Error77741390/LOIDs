#!/usr/bin/env python3

with open('/workspace/FINAL_WORKING_MERGED.txt', 'r') as f:
    content = f.read()

# Check for key components
checks = {
    "Main Mod Header": "// @name         X- Precision Client" in content,
    "getEl function": "globalThis.getEl = function(id)" in content,
    "remedyConfigs": "globalThis.remedyConfigs" in content,
    "HtmlAction class": "class HtmlAction {" in content,
    "Html class": "class Html {" in content,
    "HTML instance": "globalThis.HTML = new Html()" in content,
    "menuDiv creation": "globalThis.menuDiv = document.createElement" in content,
    "menuChatDiv creation": "globalThis.menuChatDiv = document.createElement" in content,
    "toggleMenuChat function": "globalThis.toggleMenuChat = function()" in content,
    "injectStyles function": "globalThis.injectStyles = function()" in content,
    "Fixed render loop": "requestAnimationFrame(doUpdate);" in content and "setTimeout(() => requestAnimationFrame" not in content,
    "Main mod settings": "let settings = {" in content,
    "updateGame function": "function updateGame()" in content,
}

print("=== MERGE VERIFICATION ===\n")
all_pass = True
for check, result in checks.items():
    status = "✓ PASS" if result else "✗ FAIL"
    print(f"{status}: {check}")
    if not result:
        all_pass = False

print("\n" + "="*30)
if all_pass:
    print("✓ ALL CHECKS PASSED - MOD IS READY!")
else:
    print("✗ SOME CHECKS FAILED - NEEDS FIXING")
    
# Count lines
lines = content.count('\n')
print(f"\nTotal lines: {lines}")
print(f"File size: {len(content)} chars")
