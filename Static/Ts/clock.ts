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

    // Notifica leitores de tela a cada atualização do relógio
    clockEl.setAttribute("aria-live", "polite");
    clockEl.setAttribute("aria-atomic", "true");

    const tick = (): void => {
        clockEl.textContent = getCurrentTime();
    };

    tick();
    setInterval(tick, 1000);
});
