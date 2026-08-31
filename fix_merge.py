#!/usr/bin/env python3

with open('/workspace/FINAL_WORKING_MERGED.txt', 'r') as f:
    content = f.read()

# Fix 1: Complete the toggleMenuChat function
old_toggle = '''globalThis.toggleMenuChat = function() {
    if (menuChatDiv.style.display != "none") {
        //   chatHolder.style.display = "none";
        // if (menuChatBox.value != "") {
        //commands[command.slice(1)]
        sendChat(menuChatBox.value);
        menuChatBox.value = "";
        menuChatBox.blur();
    }

globalThis.injectStyles'''

new_toggle = '''globalThis.toggleMenuChat = function() {
    if (menuChatDiv.style.display != "none") {
        if (menuChatBox.value != "") {
            sendChat(menuChatBox.value);
            menuChatBox.value = "";
            menuChatBox.blur();
        }
    } else {
        menuChatBox.focus();
    }
}

globalThis.injectStyles'''

content = content.replace(old_toggle, new_toggle)

# Fix 2: Change configs to remedyConfigs in injectStyles
content = content.replace('${configs.accentColor', '${globalThis.remedyConfigs.accentColor')
content = content.replace('${configs.outlineColor', '${globalThis.remedyConfigs.outlineColor')
content = content.replace('${configs.toggleColor', '${globalThis.remedyConfigs.toggleColor')
content = content.replace('${configs.mainColor', '${globalThis.remedyConfigs.mainColor')
content = content.replace('${configs.textColor', '${globalThis.remedyConfigs.textColor')
content = content.replace('${configs.menuColor', '${globalThis.remedyConfigs.menuColor')
content = content.replace('${configs.pinkUI', '${globalThis.remedyConfigs.pinkUI')

with open('/workspace/FINAL_WORKING_MERGED.txt', 'w') as f:
    f.write(content)

print("Fixes applied!")
