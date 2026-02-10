#!/bin/bash
set -e

CONTAINER_NAME=fase2devops
IMAGE_NAME=fase2devops

docker stop $CONTAINER_NAME || true
docker rm $CONTAINER_NAME || true

docker build -t $IMAGE_NAME .

docker run -d \
  --name $CONTAINER_NAME \
  -p 8000:8000 \
  $IMAGE_NAME

echo "Contenedor '$CONTAINER_NAME' ejecutándose en el puerto 8000"