"use strict";
const welcomeMessage = "Central inteligente do Estrutura-do-Projeto";
function setAgentOutput(message) {
    const output = document.getElementById("ai-agent-output");
    if (output) {
        output.textContent = message;
    }
}
function highlightTopic(topic) {
    const cards = document.querySelectorAll("[data-topic]");
    cards.forEach((card) => {
        card.classList.toggle("highlight", card.dataset.topic === topic);
    });
}
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: "smooth", block: "start" });
    }
}
function setFocusMode(enabled) {
    document.body.classList.toggle("focus-mode", enabled);
}
function processAgentCommand(rawCommand) {
    const command = rawCommand.trim().toLowerCase();
    if (!command) {
        setAgentOutput("Digite um comando para eu controlar o site.");
        return;
    }
    if (command.includes("backend") || command.includes("python")) {
        highlightTopic("backend");
        scrollToSection("arquitetura");
        setAgentOutput("Backend destacado: rotas, app Flask e templates principais.");
        return;
    }
    if (command.includes("frontend") || command.includes("typescript")) {
        highlightTopic("frontend");
        scrollToSection("arquitetura");
        setAgentOutput("Frontend destacado: TypeScript, assets compilados e interface visual.");
        return;
    }
    if (command.includes("autom") || command.includes("script")) {
        highlightTopic("automation");
        scrollToSection("arquitetura");
        setAgentOutput("Automação destacada: setup, lint e scripts utilitários.");
        return;
    }
    if (command.includes("teste") || command.includes("qualidade") || command.includes("pytest")) {
        highlightTopic("testing");
        scrollToSection("arquitetura");
        setAgentOutput("Qualidade destacada: testes, Ruff e validações do projeto.");
        return;
    }
    if (command.includes("deploy") || command.includes("pages") || command.includes("rodar")) {
        scrollToSection("deploy");
        setAgentOutput("Painel de execução aberto: veja setup, build e comando do servidor Flask.");
        return;
    }
    if (command.includes("foco")) {
        setFocusMode(true);
        setAgentOutput("Modo foco ativado para destacar o conteúdo principal.");
        return;
    }
    if (command.includes("restaurar") || command.includes("reset")) {
        document.querySelectorAll("[data-topic]").forEach((card) => {
            card.classList.remove("highlight");
        });
        setFocusMode(false);
        scrollToSection("topo");
        setAgentOutput("Visão restaurada. Posso destacar backend, frontend, testes ou deploy.");
        return;
    }
    if (command.includes("sobre")) {
        window.location.href = "/about";
        return;
    }
    if (command.includes("home") || command.includes("topo")) {
        scrollToSection("topo");
        setAgentOutput("Voltando ao topo da página principal.");
        return;
    }
    setAgentOutput("Comando não reconhecido. Tente: backend, frontend, testes, deploy, modo foco ou restaurar.");
}
document.addEventListener("DOMContentLoaded", () => {
    const header = document.getElementById("main-heading");
    if (header) {
        header.innerText = welcomeMessage;
    }
    const form = document.getElementById("ai-agent-form");
    const input = document.getElementById("ai-agent-input");
    const quickButtons = document.querySelectorAll("[data-agent-command]");
    if (form && input) {
        form.addEventListener("submit", (event) => {
            event.preventDefault();
            processAgentCommand(input.value);
        });
    }
    quickButtons.forEach((button) => {
        button.addEventListener("click", () => {
            var _a;
            const command = (_a = button.dataset.agentCommand) !== null && _a !== void 0 ? _a : "";
            if (input) {
                input.value = command;
            }
            processAgentCommand(command);
        });
    });
});
