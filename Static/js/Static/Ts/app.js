"use strict";
const welcomeMessage = "Bem-vindo ao Estrutura-do-Projeto!";
document.addEventListener("DOMContentLoaded", () => {
    const header = document.getElementById("main-heading");
    if (header) {
        header.innerText = welcomeMessage;
        console.log("TypeScript carregado com sucesso!");
    }
});
