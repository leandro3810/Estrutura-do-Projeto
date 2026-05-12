#!/bin/bash
# setup.sh — Configura o ambiente virtual e instala todas as dependências.
set -euo pipefail

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo -e "${GREEN}==> Criando ambiente virtual em .venv...${NC}"
python3 -m venv .venv

echo -e "${GREEN}==> Ativando ambiente e instalando dependências...${NC}"
source .venv/bin/activate
pip install --upgrade pip --quiet

if [ -f pyproject.toml ]; then
    pip install -e ".[dev]" --quiet
elif [ -f requirements.txt ]; then
    pip install -r requirements.txt --quiet
else
    echo -e "${YELLOW}Aviso: nenhum arquivo de dependências encontrado.${NC}"
fi

echo -e "${GREEN}==> Ambiente configurado com sucesso!${NC}"
echo -e "Para ativar manualmente: ${GREEN}source .venv/bin/activate${NC}"
