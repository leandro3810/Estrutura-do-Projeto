#!/bin/bash
# test.sh — Executa a suite de testes com Pytest.
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

echo -e "${GREEN}==> Executando testes com Pytest...${NC}"
pytest Tests/ -v

echo -e "${GREEN}==> Todos os testes passaram!${NC}"
