#!/bin/bash
# deploy.sh — valida e prepara o build para entrega empresarial.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "==> Rodando lint..."
bash scripts/lint.sh

echo "==> Rodando testes..."
bash scripts/test.sh

echo "==> Validando TypeScript..."
npm run build:check

echo "==> Gerando build de assets..."
npm run build

echo "==> Pacote pronto. Inicie com: flask --app python/Run.py run"
