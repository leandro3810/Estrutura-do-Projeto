/**
 * clock.ts — Componente de relógio digital em tempo real.
 * Atualiza o elemento #clock a cada segundo com hora local.
 */

function formatTwoDigits(n: number): string {
    return n.toString().padStart(2, "0");
}

function getCurrentTime(): string {
    const now = new Date();
    const h = formatTwoDigits(now.getHours());
    const m = formatTwoDigits(now.getMinutes());
    const s = formatTwoDigits(now.getSeconds());
    return `${h}:${m}:${s}`;
}

document.addEventListener("DOMContentLoaded", () => {
    const clockEl = document.getElementById("clock");
    if (!clockEl) return;

    const tick = (): void => {
        clockEl.innerText = getCurrentTime();
    };

    tick();
    setInterval(tick, 1000);
});
