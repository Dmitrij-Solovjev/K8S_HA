#!/bin/bash

docker build --no-cache . -t consumer-image:0.1
docker image save -o image.tar consumer-image:0.1
minikube image load image.tar
rm image.tar
