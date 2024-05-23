#!/bin/bash

# Crear el entorno virtual
python3 -m venv .venv

# Activar el entorno virtual
source .venv/bin/activate

# Instalar las dependencias
pip install -r requirements.txt

echo "El entorno virtual se ha configurado y las dependencias se han instalado."
