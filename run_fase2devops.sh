#!/bin/bash
set -e

# Cargar variables de entorno
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# Opcional: construir la imagen si no existe
docker image inspect fase2devops >/dev/null 2>&1 || docker build -t fase2devops .

# Detener contenedor previo si existe
docker stop fase2devops-container >/dev/null 2>&1 || true
docker rm fase2devops-container >/dev/null 2>&1 || true

# Ejecutar contenedor en segundo plano (sin -it)
docker run \
  --name fase2devops-container \
  -e GITHUB_TOKEN="$GITHUB_TOKEN" \
  fase2devops