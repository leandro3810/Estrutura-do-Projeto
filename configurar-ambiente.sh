#!/bin/bash

# Cores para saída
GREEN='\033[0;32m'
NC='\033[0m' # Sem cor

echo -e "${GREEN}==> Configurando o ambiente virtual...${NC}"
python3 -m venv .venv

echo -e "${GREEN}==> Ativando o ambiente e instalando dependências...${NC}"
source .venv/bin/activate

# Instala as dependências listadas no requirements.txt
if [ -f requirements.txt ]; then
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "requirements.txt não encontrado. Instalando dependências básicas..."
    pip install flask ruff
fi

echo -e "${GREEN}==> Ambiente configurado com sucesso!${NC}"
echo -e "Para ativar manualmente, use: ${GREEN}source .venv/bin/activate${NC}"
