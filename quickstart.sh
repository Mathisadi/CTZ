#!/bin/bash
set -e
# quickstart.sh - Démarrage rapide du programme Python dans un sous-dossier

# Obtenir le dossier où se trouve ce script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Vérifier si l'environnement virtuel existe et l'activer, sinon le créer et installer les dépendances
if [ -f "$SCRIPT_DIR/.venv/bin/activate" ]; then
    echo "Activation de l'environnement virtuel..."
    source "$SCRIPT_DIR/.venv/bin/activate"
else
    echo "L'environnement virtuel n'existe pas. Création d'un nouvel environnement..."
    python3 -m venv "$SCRIPT_DIR/.venv"
    source "$SCRIPT_DIR/.venv/bin/activate"
    echo "Installation des dépendances..."
    pip install --upgrade pip
    if [ -f "$SCRIPT_DIR/requirements.txt" ]; then
      pip install -r "$SCRIPT_DIR/requirements.txt"
    fi
fi

# Construire le chemin complet vers le fichier Python dans le sous-dossier "src"
cd "$SCRIPT_DIR"

# Vérifier que le fichier existe
python -c "from Data import *; clear_res()"
python -c "from Data import *; clear_data()"

# On lance l'API
cd "$SCRIPT_DIR/Api/"

fastapi dev Main.py &
BACKEND_PID=$!

cd "$SCRIPT_DIR"
# On lance le front

cd "$SCRIPT_DIR/Interface/"

npm run dev &
FRONTEND_PID=$!

