#!/bin/bash

# Cores para logs
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}==> Iniciando o aplicativo Flask...${NC}"

# Verifica se o ambiente virtual existe
if [ -d ".venv" ]; then
    source .venv/bin/activate
elif [ -d "venv" ]; then
    source venv/bin/activate
else
    echo -e "${YELLOW}Aviso: Ambiente virtual não encontrado. Rodando com o python do sistema...${NC}"
fi

# Define a variável de ambiente para o Flask apontar para o arquivo correto
export FLASK_APP=python/Run.py
export FLASK_ENV=development

# Executa o servidor
python3 python/Run.py
