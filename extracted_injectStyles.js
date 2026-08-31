globalThis.injectStyles = function() {
    const existingStyle = document.getElementById("remedy-theme-styles");
    if (existingStyle) existingStyle.remove();
    const styleElement = document.createElement("style");
    styleElement.id = "remedy-theme-styles";
    styleElement.innerHTML = `
    :root {
        --primary-color: ${configs.accentColor || (configs.pinkUI ? "#ff9cfb" : "#50afef")};
        --outline-color: ${configs.outlineColor || "#e0e0e0"};
        --secondary-color: var(--outline-color);
        --toggle-color: ${configs.toggleColor || "#494b48"};
        --background-color: ${configs.mainColor || (configs.pinkUI ? "rgb(93 0 131 / 40%)" : "rgba(0, 0, 0, 0.7)")};
        --foreground-color: ${configs.textColor || "#e0e0e0"};
        --menu-background-color: ${configs.menuColor || "#000000b7"};
        --selection-color: #494b48;
    }
    input[type="range"] {
        -webkit-appearance: none;
        appearance: none;
        height: 2px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 999px;
        outline: none;
    }
    input[type="range"]::-webkit-slider-runnable-track {
        height: 4px;
        border-radius: 4px;
        background:
            linear-gradient(
                to right,
                var(--toggle-color) 0%,
                var(--toggle-color) var(--slider-fill, 0%),
                rgba(255, 255, 255, 0.08) var(--slider-fill, 0%),
                rgba(255, 255, 255, 0.08) 100%
            );
    }

    input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        margin-top: -5px;
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background: var(--foreground-color);
        border: none;
        cursor: pointer;
    }

    input[type="range"]::-moz-range-thumb {
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background: var(--foreground-color);
        border: none;
        cursor: pointer;
    }

    input[type="range"]::-moz-range-thumb {
        background: var(--foreground-color);
    }

    #menu-info-tooltip {
        display: none;
        position: fixed;
        z-index: 1000000;
        max-width: 240px;
        padding: 10px;
        background: rgba(0, 0, 0, 0.88);
        color: var(--foreground-color);
        border: 1px solid var(--primary-color);
        border-radius: 8px;
        box-shadow: rgba(0, 0, 0, 0.35) 0px 6px 12px;
        pointer-events: none;
        font-size: 12px;
        line-height: 1.3;
        transition: opacity 180ms ease;
    }
    .colored-icon {
        background-color: var(--toggle-color);
        mask: var(--icon) center / contain no-repeat;
        -webkit-mask: var(--icon) center / contain no-repeat;
    }
    .menu-info-tooltip-title {
        font-weight: bold;
        margin-bottom: 4px;
        color: var(--primary-color);
    }

    .menu-info-tooltip-body {
        position: relative;
        opacity: 0.9;
    }

    .has-info-tooltip {
        cursor: help;
    }

    .menu-action-button {
        width: 100%;
        height: 32px;
        margin-bottom: 10px;
        background: rgba(255, 255, 255, 0.07);
        color: var(--foreground-color);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 8px;
        cursor: pointer;
        text-align: center;
    }

    .menu-action-button:hover {
        background: rgba(255, 255, 255, 0.14);
    }

    .advanced-popup-overlay {
        position: fixed;
        inset: 0;
        z-index: 999999;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(0, 0, 0, 0.45);
    }

    .advanced-popup-window {
        width: 620px;
        max-height: 460px;
        background: var(--menu-background-color);
        color: var(--foreground-color);
        border: var(--border);
        border-radius: 8px;
        box-shadow: rgba(0, 0, 0, 0.4) 0px 8px 16px 0px;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        padding: 10px;
    }

    .advanced-popup-topbar {
        height: 133px;
        display: flex;
        align-items: center;
        flex-direction: column;
        padding: 1px 0px 6px 0px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }

    .advanced-popup-title {
        position: relative;
        top: 4px;
        font-size: 15px;
        font-weight: bold;
    }

    .advanced-popup-disclaimer {
        top: 14px;
        text-align: center;
        position: relative;
        padding: 0px, 94px, 0px, 94px;
    }

    .advanced-popup-close {
        position: absolute;
        align-self: end;
        width: 30px;
        height: 30px;
        background: rgba(255, 255, 255, 0.08);
        color: var(--foreground-color);
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 22px;
        line-height: 1;
    }

    .advanced-popup-close:hover {
        background: rgba(255, 255, 255, 0.16);
    }

    .advanced-popup-content {
        padding: 12px;
        overflow-y: auto;
        scrollbar-width: none;
    }

    .advanced-weight-group {
        margin-bottom: 14px;
    }

    .advanced-weight-group .switch-container {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 9px;
    }

    .advanced-weight-group .switch-label-text {
        flex: 1;
        min-width: 0;
    }
    #menuChatDiv {
        border-radius: 6.7px;
        scrollbar-width: none;
        box-shadow: none;
    }
    #storeButton {
        display: none !important;
        position: fixed !important;
        top: 20px !important;
        right: 280px !important;
        left: auto !important;
        bottom: auto !important;
        z-index: 20 !important;
    }
    #allianceButton,
    #partyButton,
    #partyJoinButton,
    #joinPartyButton,
    #allianceMenu {
        display: none !important;
        visibility: hidden !important;
        pointer-events: none !important;
    }
    #killCounter {
        margin-top: 10px;
    }

    #ageBarBody {
        border-radius: 8px;
    }
    .actionBarItem, #ageBar, #chatBox {
        border: var(--border);
        box-shadow: rgba(0, 0, 0, 0.6) 0px 6px 12px 0px;
        background-color: var(--background-color);
        border-radius: 8px;
    }
    #mChBox {
        text-align: center;
        border-radius: 8px;
        background: rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.2)
    }

    #killCounter, #scoreDisplay, #foodDisplay, #woodDisplay, #stoneDisplay {
        background-image: none;
        padding: 0px 8px;
        margin: 0px;
        text-align: center;
    }
    #menuCardHolder {
        display: block;
        position: absolute;
        top: 50%;
        left: 50%;
        translate: transition(-50%, -50%);
        transform: translate(-50%, -30%);
    }
    #loadingText {
        position: absolute;
        left: 50%;
        transform: translate(-50%, -230%);
    }
    #gameName {
        font-size: 120px;
        text-shadow: none;
        font-weight: black;
        positon: absolute;
        position: absolute;
        transform: translate(-50%, -230%);
        top: 50%;
        left: 50%;
    }
    #setupCard, #guideCard, #enterGame, #storeButton, #allianceButton, #foodDisplay,
    #woodDisplay, #killCounter, #stoneDisplay, #scoreDisplay, #mapDisplay, #leaderboard {
        border: var(--border);
        border-image-slice: 1;
        box-shadow: rgba(0, 0, 0, 0.6) 0px 6px 12px 0px;
        background: var(--background-color);
        border-radius: 6px;
    }
    #menuChatDiv {
        backdrop-filter: blur(3px);
        top: 10px;
        left: 10px;
        scrollbar-width: none;
        box-shadow: none;
        background: rgba(0, 0, 0, 0.2);
    }
    #mChDiv {
        background-color: rgba(0, 0, 0, 0);
    }
    .menuHeader {
        color: white;
        text-align: center;
    }
    #menu-container {
        width: 700px;
        height: 500px;
        background: var(--menu-background-color);
        color: var(--foreground-color);
        font-family: Arial, sans-serif;
        padding: 10px;
        box-shadow: rgba(0, 0, 0, 0.24) 0px 6px 12px 0px;
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        display: flex;
        flex-direction: row;
        visibility: visible;
        opacity: 1;
        transition: opacity 0.3s ease;
        border: var(--border);
        border-image-slice: 1;
        border-radius: 6px;
    }
    .menu-image-overlay {
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        flex-wrap: wrap;
        max-width: 1200px;
        gap: 12px;
        z-index: 9999;
        padding: 6px;
        pointer-events: none;
        justify-content: center;
    }
    .menu-image-item {
        position: relative;
        width: 54.44px;
        height: 54.44px;
        padding: 0;
        background: var(--background-color);
        border-radius: 14px;
        border: var(--border);
        overflow: hidden;
        pointer-events: auto;
    }
    .menu-image-overlay .menu-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border: none;
        border-radius: 0;
        display: block;
        cursor: pointer;
    }
    .menu-image-overlay .menu-image-label {
        position: absolute;
        left: 8px;
        right: 8px;
        bottom: 8px;
        background: var(--background-color);
        color: var(--foreground-color);
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        text-align: center;
        border-radius: 6px;
        pointer-events: none;
    }
    #menu-container .feature-panel, #menu-container .left-panel {
        height: 100%;
        background: rgb(93 0 131 / 7%);
        padding: 10px;
        box-sizing: border-box;
        border: none;
        border-radius: 6px;
    }
    #menu-container .feature-panel {
        width: 70%;
        margin-left: 10px;
    }
    #menu-container .left-panel {
        width: 30%;
    }
    #menu-container .left-panel .left-title {
        display: flex;
        justify-content: center;
    }
    #menu-container .left-panel .left-title span {
        font-size: 16px;
        color: var(--foreground-color);
        margin-bottom: 2px;
    }
    #menu-container .left-panel .left-title .version {
        font-size: 15px;
        margin-left: 10px;
        text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #fff,
                    0 0 40px #00f, 0 0 70px #00f, 0 0 80px #00f,
                    0 0 100px #00f, 0 0 150px #00f;
    }
    #menu-container .left-panel button {
        padding: 8px;
        margin: 5px 0;
        width: 100%;
        background: rgba(0, 0, 0, 0.1);
        color: var(--foreground-color);
        border: none;
        cursor: pointer;
        text-align: left;
        outline: none;
        display: flex;
        align-items: center;
        transition: opacity 0.3s ease;
        opacity: 0.8;
        border-radius: 6px;
    }
    #menu-container .left-panel button:hover, #menu-container .left-panel button:focus {
        background: rgba(255, 255, 255, 0.2);
        opacity: 1;
    }
    #menu-container .left-panel button.active {
        background: rgba(0, 0, 0, 0.25);
        opacity: 1;
    }
    #menu-container .active-panel {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        align-content: start;
    }
    #menu-container .placers-panel.active-panel,
    #menu-container .clans-panel.active-panel,
    #menu-container .joinrequests-panel.active-panel {
        display: block !important;
    }
    .checkbox-label {
        font-size: 14px;
        color: var(--foreground-color);
        margin-left: 5px;
    }
    .section-header {
        color: var(--foreground-color);
        font-size: 12px;
        text-transform: uppercase;
        margin-top: 12px;
        margin-bottom: 8px;
        opacity: 0.7;
        grid-column: 1 / -1;
        letter-spacing: 0.5px;
    }
    .switch-container {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
        gap: 10px;
    }
    .switch-container.switch-right {
        grid-column: 2 / 3;
        grid-row: auto;
    }
    .switch-label-text {
        color: var(--foreground-color);
        font-size: 14px;
        flex: 1;
        white-space: normal;
        word-wrap: break-word;
        line-height: 1.2;
    }
    .switch-checkbox {
        display: none;
    }
    .switch-label {
        display: inline-block;
        width: 40px;
        height: 24px;
        background-color: rgba(0, 0, 0, 0.2);
        box-shadow: rgba(0, 0, 0, 0.6) 0px 0px 4px;
        position: relative;
        transition: background-color 0.3s ease;
        border-radius: 32px;
        border: none;
    }
    .switch-label::before {
        content: '';
        position: absolute;
        top: 1px;
        left: 1px;
        width: 22px;
        height: 22px;
        background-color: white;
        transition: left 0.3s ease;
        border-radius: 32px;
    }
    /* When checkbox is checked (toggle ON) */
    .switch-checkbox:checked + .switch-label {
        background-color: var(--toggle-color); /* Green when on */
        box-shadow: var(--toggle-color) 0px 0px 2px;
    }
    .switch-checkbox:checked + .switch-label::before {
        left: 18px; /* Move the knob to the right */
    }
    #altcha {
        color: white;
    }
    #killCounter {
        margin-top: 10px;
    }
    #menuChatDiv {
        backdrop-filter: blur(5px);
        scrollbar-width: none;
        box-shadow: none;
    }
    #enterGame {
    background: rgb(6, 135, 63);
    padding: 8px;
    border: none;
    }
    .altcha svelte-ddsc3z {
        background: #eb90ff;
        border-radius: 8px;
        width: 283.25px;
        border: none;
        padding: 0.8rem
    }
    .skinColorItem {
        border: 0px;
    }

    #skinColorHolder {
        display: grid;
        justify-content: center;
        align-items: center;
        grid-auto-flow: column;
    }
    #guideCard {
        max-height: 700px;
        width: 500px;
        overflow-y: hidden;
    }
    #setupCard {
        width: 500px;
        height: 700px;
    }
    #nameInput {
    border-radius: 8px;
    }
`;
    document.head.appendChild(styleElement);
}