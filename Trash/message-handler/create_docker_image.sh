#!/bin/bash

docker build --no-cache . -t message-handler-image:0.1
docker image save -o image.tar message-handler-image:0.1
minikube image load image.tar
rm image.tar
