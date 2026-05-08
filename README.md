# Estrutura do Projeto Flask 🚀

Este repositório contém uma estrutura organizada para o desenvolvimento de aplicações web utilizando **Flask** (Python) e **TypeScript** (JS).

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python com Flask.
- **Frontend:** HTML5, CSS3 e TypeScript.
- **Ferramentas:** Ruff (Linter/Formatter) e Shell scripts para automação.

## 🚀 Como Configurar o Ambiente

Para facilitar a configuração do ambiente virtual e instalação das dependências, utilize os scripts inclusos:

### No Linux/macOS:
```bash
bash configurar-ambiente.sh
```
Isso criará a pasta `.venv`, ativará o ambiente e instalará o Flask e o Ruff automaticamente.

### Ativação Manual:
```bash
source .venv/bin/activate
```

## 💻 Como Rodar o Projeto

1. Certifique-se de que o ambiente virtual está ativado.
2. Execute o servidor:
   ```bash
   flask --app python/Run.py run --debug
   ```
3. Acesse em seu navegador: `http://127.0.0.1:5000`

## 📁 Estrutura de Pastas Principais

- `python/`: Contém a lógica do servidor e rotas.
- `templates/`: Arquivos HTML do projeto.
- `Static/`: Arquivos estáticos (CSS, JS, Imagens).
- `requirements.txt`: Lista de dependências Python.

---
Desenvolvido por [leandro3810](https://github.com/leandro3810).
