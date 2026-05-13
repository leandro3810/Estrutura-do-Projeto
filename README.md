# Estrutura do Projeto Flask 🚀

Base full-stack com **Flask + TypeScript** para construir, validar, entregar e evoluir um projeto web do início ao fim.

## 1) Definição e Escopo

- **Objetivo:** manter uma estrutura clara para backend, frontend, testes e automações.
- **Público-alvo:** desenvolvedores que precisam iniciar e escalar um projeto web organizado.
- **MVP atual:**
  - Rotas web `/` e `/about`
  - Rota de saúde `/health`
  - Templates com dados dinâmicos do backend
  - Build TypeScript e scripts de validação

### Requisitos Funcionais
- Renderizar páginas principais com Flask.
- Servir assets estáticos compilados.
- Expor endpoint de saúde para monitoramento.
- Executar lint e testes automatizados.

### Requisitos Não Funcionais
- Segurança básica com `SECRET_KEY` via variável de ambiente.
- Build reproduzível com scripts padronizados.
- Qualidade mínima com Ruff + Pytest + checagem TypeScript.

### Critérios de Aceite
- Setup finaliza sem erros.
- Rotas principais respondem `200`.
- Rota inexistente responde erro consistente.
- CI executa lint, testes e build/check.

## 2) Estrutura Base do Repositório

- `python/` → app Flask (fábrica, rotas, config e serviços)
- `templates/` → páginas e erros
- `Static/` → CSS, JS compilado e TS fonte
- `scripts/` → `setup.sh`, `lint.sh`, `test.sh`
- `Tests/` → testes automatizados
- `.github/workflows/` → CI e automações agendadas

## 3) Preparação do Ambiente

```bash
bash scripts/setup.sh
```

O script cria `.venv`, instala dependências Python e Node/TypeScript.

## 4) Fluxo Local Único (Construção)

1. **Setup:** `bash scripts/setup.sh`
2. **Build TS:** `npm run build`
3. **Executar Flask:** `flask --app python/Run.py run --debug`
4. **Qualidade:** `bash scripts/lint.sh && bash scripts/test.sh`
5. **Segurança de dependências:** `source .venv/bin/activate && pip check && npm audit --audit-level=high`

## 5) Backend (Flask)

- Fábrica do app em `python/__init__.py`
- Rotas em `python/routes.py`
- Configuração em `python/config.py`
- Serviço de dados de apresentação em `python/services/project_overview.py`
- Tratamento de erros HTTP e fallback em templates de erro

## 6) Frontend (Templates + Assets)

- Base em `templates/base.html`
- Páginas principais: `templates/index.html` e `templates/about.html`
- Assets em `Static/style.css`, `Static/Ts/`, `Static/js/`
- TypeScript compilado para `Static/js/`

## 7) Qualidade e Testes

- Lint/format: `bash scripts/lint.sh`
- Testes: `bash scripts/test.sh`
- Build check TS: `npm run build:check`

## 8) CI/CD

- CI de validação em PR/push para main: `.github/workflows/ci.yml`
- Workflow agendado de issues: `.github/workflows/report-issues.yaml`
- Recomenda-se branch protection exigindo os checks de CI antes de merge

## 9) Segurança e Governança

- Defina `SECRET_KEY` no ambiente de execução.
- Para produção, defina também `SESSION_COOKIE_SECURE=1`.
- O app aplica cabeçalhos de segurança por padrão:
  - `X-Content-Type-Options: nosniff`
  - `X-Frame-Options: DENY`
  - `Referrer-Policy: strict-origin-when-cross-origin`
  - `Content-Security-Policy` restritiva para recursos locais
- Revise dependências periodicamente.
- Valide dependências com:
  - `source .venv/bin/activate && pip check`
  - `npm audit --audit-level=high`
- Mantenha:
  - `SECURITY.md`
  - `CODE_OF_CONDUCT.md`
  - templates em `.github/ISSUE_TEMPLATE/`

## 10) Entrega e Deploy

- Build validado (`build:check`, lint e testes)
- Variáveis de ambiente configuradas
- Comando de execução definido
- Checklist de release com validação funcional e plano de rollback

## 11) Operação Pós-Entrega

- Monitorar disponibilidade via `/health`
- Revisar logs e falhas de execução
- Manter rotina de atualização de dependências e testes de regressão

## 12) Evolução Contínua

- Planejar roadmap (MVP → v1 → v2)
- Refatorar módulos de crescimento
- Expandir testes e documentação a cada funcionalidade nova

---
Desenvolvido por [leandro3810](https://github.com/leandro3810).
