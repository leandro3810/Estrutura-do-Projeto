const welcomeMessage: string = "Olá do TypeScript!";

document.addEventListener("DOMContentLoaded", () => {
    const header = document.querySelector("h1");
    if (header) {
        header.innerText = welcomeMessage;
        console.log("TypeScript carregado com sucesso!");
    }
});
