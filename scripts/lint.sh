#!/bin/bash
# lint.sh — Executa o Ruff para verificar e formatar o código Python.
set -euo pipefail

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# Ativa o ambiente virtual se existir
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

echo -e "${GREEN}==> Verificando código com Ruff...${NC}"
ruff check python/ Tests/

echo -e "${GREEN}==> Formatando código com Ruff...${NC}"
ruff format python/ Tests/

echo -e "${GREEN}==> Lint concluído sem erros.${NC}"
