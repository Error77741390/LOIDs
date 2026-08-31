globalThis.toggleMenuChat = function() {
    if (menuChatDiv.style.display != "none") {
        //   chatHolder.style.display = "none";
        // if (menuChatBox.value != "") {
        //commands[command.slice(1)]
        sendChat(menuChatBox.value);
        menuChatBox.value = "";
        menuChatBox.blur();
    } else {
        if (menuCBFocus) menuChatBox.blur();
        else menuChatBox.focus();
    }
}
globalThis.keyDown = function(event) {
    let keyNum = event.which || event.keyCode || 0;
    if (event.key == "Enter") {
        toggleChat();
        keys[keyNum] = 1;
        macro.Enter = 1;
        return;
    }
    if (
        player &&
        player.alive &&
        keysActive() &&
        chatHolder.style.display === "none"
    ) {
        if (
            chatHolder.style.display == "block" ||
            textAreas.includes(document.activeElement.id)
        )
            return;
        if (!keys[keyNum]) {
            keys[keyNum] = 1;
            macro[event.key] = 1;
            if (event.key == "i") {
                if (player.team) {
                    const wasOwner = player.isOwner, oldTeam = player.team;
                    packet("N");
                    setTimeout(() => {
                        packet("L", "owNer");
                        game.tickBase(() => {
                            packet("6", "close your eyes");
                            game.tickBase(() => {
                                packet("N");
                                game.tickBase(() => {
                                    if (oldTeam !== null) {
                                        if (wasOwner) packet("L", oldTeam);
                                        else packet("b", oldTeam);
                                    }
                                }, 6)
                            }, 3);
                        }, 3)
                    }, 500)
                } else {
                    packet("L", "owNer");
                    game.tickBase(() => {
                        packet("6", "close your eyes");
                        game.tickBase(() => {
                            packet("N");
                        }, 4);
                    }, 2)
                }
            } else if (!event.ctrlKey && keyNum == 16) {
                // break function here
                /*if ([13, 12, 9].includes(player.secondaryIndex)) {
                    consolelog(game.tick)
                    consolelog(game.tick)
                    consolelog(game.tick)
                    consolelog("BOOST TICK")
                    game.tickBase(() => {
                        consolelog(game.tick)
                        instaC.boostTickType("boost1");
                    }, 1);
                } else {
                    consolelog("NORMAL")
                    game.tickBase(() => {
                        oneTick(1, 1);
                    }, 1)
                }*/
            } else if (event.key == "t") oneTick()
            else if (event.key == "F5") {
                event.preventDefault();
                hacking = !hacking;
                if (!hacking) {
                    sendWS = sendWS2;
                } else {
                    sendWS = sendWS1;
                }
            } else if (event.key == "j") autoQuadSpike = !autoQuadSpike;
            else if (event.key == "F8") event.preventDefault();
            else if (keyNum == 226 && playerHasPolearm) oneTicking = true;
            else if (event.key == "r") waitInsta = !waitInsta;
            else if (keyNum == 69) {
                manualAutoGather = !manualAutoGather;
                sendAutoGather("e");
            } else if (keyNum == 67) updateMapMarker();
            else if (keyNum == 49) selectWeapon2(player.primaryIndex);
            else if (keyNum == 50) {
                if (player.secondaryIndex) selectWeapon2(player.secondaryIndex)
                else packet2("z", player.items[0], null, 1, "selectItem"), hold = [player.items[0], null, 1];
            } else if (keyNum == 51) {
                const theItem = (player.secondaryIndex ? player.items[0] : player.items[1]);
                packet2("z", theItem, null, 1, "selectItem");
                hold = [theItem, null, 1];
            } else if (keyNum == 53) {
                const theItem = (player.secondaryIndex ? player.items[2] : player.items[3])
                if (theItem) packet2("z", theItem, null, 1, "selectItem"), hold = [theItem, null, 1];
            } else if (keyNum == 54) {
                const theItem = (player.secondaryIndex ? player.items[3] : player.items[4])
                if (theItem) packet2("z", theItem, null, 1, "selectItem"), hold = [theItem, null, 1];
            } else if (keyNum == 55) {
                const theItem = (player.secondaryIndex ? player.items[4] : player.items[5])
                if (theItem) packet2("z", theItem, null, 1, "selectItem"), hold = [theItem, null, 1];
            } else if (keyNum == 56) {
                const theItem = (player.secondaryIndex ? player.items[5] : player.items[6])
                if (theItem) packet2("z", theItem, null, 1, "selectItem"), hold = [theItem, null, 1];
            } else if (keyNum == 57) {
                const theItem = (player.secondaryIndex ? player.items[6] : player.items[7])
                if (theItem) packet2("z", theItem, null, 1, "selectItem"), hold = [theItem, null, 1];
            } else if (event.key == "q" && !globalThis.hacking) {
                packet2("z", player.items[0], null, 1, "selectItem"), hold = [player.items[0], null, 1];
            } else if (event.key == "0") {
                if (globalThis.hacking) {
                    mills.placeSpawnPads = !mills.placeSpawnPads;
                    textManager.showText(mouseX, mouseY, 40, 1, "AutoSpawnPads", false, "white");
                    textManager.showText(mouseX, mouseY + 40, 40, 1, mills.placeSpawnPads ? "Enabled" : "Disabled", false, "white");
                } else {
                    const theItem = (player.secondaryIndex ? player.items[9] : player.items[8])
                    if (theItem) packet2("z", theItem, null, 1, "selectItem")
                }
            } else if (event.key == "g") spikeTickInsta();
            else if (event.key == "x") {
                if (!globalThis.hacking) packet2("K", 0);
                else my.reSync = true;
            }else if (event.key == "m") {
                mills.place = !mills.place;
                textManager.showText(mouseX, mouseY, 40, 1, "Auto Mills", false, "white");
                textManager.showText(mouseX, mouseY + 40, 40, 1, mills.place ? "Enabled" : "Disabled", false, "white");
            } else if (event.key == "Z") typeof window.debug == "function" && window.debug();
            else if (keyNum == 32) {
                if (!globalThis.hacking) packet2("F", 1, getVisualDir(), 1)
            } else if (event.key == ".") {
                spike = false;
                moveslikejagger = true;
                active = true;
                boostSpike = true;
                quaded = false;
                boost2 = false;
                boost3 = false;
                boost4 = false;
                loopBoostSpike = true;
                savedAim = undefined;
            } else if (event.key == "l") {
                packet("F", 1, getVisualDir(), 1, "l");
                packet("F", 0, getVisualDir(), 1, "l");
            }
        }
    }
}
window.addEventListener("keydown", checkTrustedInput(keyDown));
// let yy = canvaz.height/2;
// let mouze = {
//     x: xx - mouzeX,
//     y: yy - mouzeY
// }
// let ingamecoorformodabow = {
//     x: player.x + mouze.x,
//     y: player.x + mouze.x
// }
globalThis.keyUp = function(event) {
    let keyNum = event.which || event.keyCode || 0;
    if (keyNum == 226) oneTicking = false;
    else if (keyNum == 32) {
        if (!globalThis.hacking) packet2("F", 0, getVisualDir(), 1)
    }
    if (
        player &&
        player.alive &&
        chatHolder.style.display === "none"
    ) {
        if (chatHolder.style.display == "block" || textAreas.includes(document.activeElement.id)) return;
        if (keysActive()) {
            if (keys[keyNum]) {
                keys[keyNum] = 0;
                macro[event.key] = 0;
                if (event.key == ".") boostSpike = false;
            }
        }
    }
}
window.addEventListener("keyup", UWUTILS.checkTrusted(keyUp));
globalThis.lastMoveDirTime = performance.now();
globalThis.savedDir = null;
globalThis.sendMoveDir = function() {
    if (noMove || game.tick == lastMove) return;
    if (chatHolder.style.display != "block") savedDir = getMoveDir();
    let p2 = { x2: player.x2, y2: player.y2, xVel: player.xVel, yVel: player.yVel}
    p2.buildIndex = -1;
    p2.tailIndex = player.predictTail;
    p2.skinIndex = player.predictta;
    p2.weaponIndex = player.weaponIndex;
    let newMoveDir = savedDir;
    const vel = calcVelNoCollision(p2, newMoveDir, { maxSpeed: Math.max(1.2, player.maxSpeed) }, 1);
    if (nearHacker.hitSpike && squareDist(vel.accel.x - nearHacker.x2, vel.accel.y - nearHacker.y2) <= 8100) newMoveDir = undefined;
    runInto(player, newMoveDir, vel);
    /*} else consolelog("not breaking", player.predictSpeedMult)*/
    if (!oneTicking) {
        lastMove = game.tick;
        lastMoveDir = newMoveDir;
    }
    player.moveDirection = newMoveDir;
    player.moveSin = newMoveDir == undefined || newMoveDir == null ? 0 : sin(newMoveDir);
    player.moveCos = newMoveDir == undefined || newMoveDir == null ? 0 : cos(newMoveDir);
    updatePredictPos(null, 6, null);
}