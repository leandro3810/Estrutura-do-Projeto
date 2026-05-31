const staticWelcomeMessage = "Central inteligente do Estrutura-do-Projeto";

function setStaticAgentOutput(message) {
    const output = document.getElementById("ai-agent-output");
    if (output) {
        output.textContent = message;
    }
}

function highlightStaticTopic(topic) {
    document.querySelectorAll("[data-topic]").forEach((card) => {
        card.classList.toggle("highlight", card.dataset.topic === topic);
    });
}

function scrollStaticSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: "smooth", block: "start" });
    }
}

function setStaticFocusMode(enabled) {
    document.body.classList.toggle("focus-mode", enabled);
}

function processStaticAgentCommand(rawCommand) {
    const command = rawCommand.trim().toLowerCase();

    if (!command) {
        setStaticAgentOutput("Digite um comando para eu controlar o site.");
        return;
    }

    if (command.includes("backend") || command.includes("python")) {
        highlightStaticTopic("backend");
        scrollStaticSection("arquitetura");
        setStaticAgentOutput("Backend destacado: Flask, rotas e templates.");
        return;
    }

    if (command.includes("frontend") || command.includes("typescript")) {
        highlightStaticTopic("frontend");
        scrollStaticSection("arquitetura");
        setStaticAgentOutput("Frontend destacado: TypeScript, CSS e agente local.");
        return;
    }

    if (command.includes("autom") || command.includes("script")) {
        highlightStaticTopic("automation");
        scrollStaticSection("arquitetura");
        setStaticAgentOutput("Automação destacada: setup, lint e scripts auxiliares.");
        return;
    }

    if (command.includes("teste") || command.includes("qualidade") || command.includes("pytest")) {
        highlightStaticTopic("testing");
        scrollStaticSection("arquitetura");
        setStaticAgentOutput("Qualidade destacada: Pytest, Ruff e validações do projeto.");
        return;
    }

    if (command.includes("deploy") || command.includes("pages") || command.includes("rodar")) {
        scrollStaticSection("deploy");
        setStaticAgentOutput("Área de deploy aberta com os comandos principais do projeto.");
        return;
    }

    if (command.includes("foco")) {
        setStaticFocusMode(true);
        setStaticAgentOutput("Modo foco ativado.");
        return;
    }

    if (command.includes("restaurar") || command.includes("reset")) {
        document.querySelectorAll("[data-topic]").forEach((card) => {
            card.classList.remove("highlight");
        });
        setStaticFocusMode(false);
        scrollStaticSection("topo");
        setStaticAgentOutput("Visão restaurada. Tente backend, frontend, testes ou deploy.");
        return;
    }

    if (command.includes("sobre")) {
        window.location.href = "About.html";
        return;
    }

    if (command.includes("home") || command.includes("topo")) {
        scrollStaticSection("topo");
        setStaticAgentOutput("Voltando ao topo da página.");
        return;
    }

    setStaticAgentOutput("Comando não reconhecido. Tente: backend, frontend, testes, deploy, modo foco ou restaurar.");
}

function updateStaticClock() {
    const clock = document.getElementById("clock");
    if (!clock) {
        return;
    }

    const now = new Date();
    const hour = `${now.getHours()}`.padStart(2, "0");
    const minute = `${now.getMinutes()}`.padStart(2, "0");
    const second = `${now.getSeconds()}`.padStart(2, "0");
    clock.textContent = `${hour}:${minute}:${second}`;
    clock.setAttribute("datetime", now.toISOString());
}

document.addEventListener("DOMContentLoaded", () => {
    const header = document.getElementById("main-heading");
    if (header) {
        header.textContent = staticWelcomeMessage;
    }

    updateStaticClock();
    window.setInterval(updateStaticClock, 1000);

    const form = document.getElementById("ai-agent-form");
    const input = document.getElementById("ai-agent-input");

    if (form && input instanceof HTMLInputElement) {
        form.addEventListener("submit", (event) => {
            event.preventDefault();
            processStaticAgentCommand(input.value);
        });
    }

    document.querySelectorAll("[data-agent-command]").forEach((button) => {
        button.addEventListener("click", () => {
            const command = button.getAttribute("data-agent-command") || "";
            if (input instanceof HTMLInputElement) {
                input.value = command;
            }
            processStaticAgentCommand(command);
        });
    });
});
