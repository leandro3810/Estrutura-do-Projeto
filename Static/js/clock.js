"use strict";
function formatTwoDigits(n) {
    return n.toString().padStart(2, "0");
}
function getCurrentTime() {
    const now = new Date();
    const h = formatTwoDigits(now.getHours());
    const m = formatTwoDigits(now.getMinutes());
    const s = formatTwoDigits(now.getSeconds());
    return `${h}:${m}:${s}`;
}
document.addEventListener("DOMContentLoaded", () => {
    const clockEl = document.getElementById("clock");
    if (!clockEl) {
        return;
    }
    clockEl.setAttribute("aria-live", "polite");
    clockEl.setAttribute("aria-atomic", "true");
    const tick = () => {
        clockEl.textContent = getCurrentTime();
    };
    tick();
    setInterval(tick, 1000);
});
