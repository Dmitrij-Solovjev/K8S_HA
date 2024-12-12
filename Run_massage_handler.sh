#!/bin/bash

#minikube start
#kubectl delete all --all
cd message-handler
./create_docker_image.sh
cd ..

kubectl apply -f ./message-handler/deployment.yaml
sleep 1
kubectl apply -f ./message-handler/service.yaml
sleep 1


#kubectl apply -f ./frontend/frontend-deployment.yaml
#sleep 1
#kubectl apply -f ./frontend/frontend-service.yaml
#sleep 0.5
kubectl get all
minikube service list
