from datetime import UTC, datetime


def get_project_overview():
    return {
        "app_name": "Estrutura-do-Projeto",
        "updated_at": datetime.now(UTC).strftime("%d/%m/%Y %H:%M UTC"),
        "mvp_features": [
            "Navegação por páginas Home e Sobre",
            "Painel com comandos rápidos no frontend",
            "Build TypeScript com saída em Static/js",
            "Scripts de setup, lint e testes automatizados",
        ],
        "build_steps": [
            "bash scripts/setup.sh",
            "npm run build",
            "flask --app python/Run.py run --debug",
            "bash scripts/lint.sh && bash scripts/test.sh",
        ],
    }
