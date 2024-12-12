#!/bin/bash

#minikube start
kubectl delete all --all

###Install the RabbitMQ operator 
kubectl apply -f https://github.com/rabbitmq/cluster-operator/releases/latest/download/cluster-operator.yml
###Check if the components are healthy in the rabbitmq-system namespace
kubectl get all -o wide -n rabbitmq-system
sleep 1
kubectl apply -f rabbitmqcluster.yaml
#kubectl get all -l app.kubernetes.io/part-of=rabbitmq
#kubectl get svc production-rabbitmqcluster -o jsonpath='{.status.loadBalancer.ingress[0].ip}'

#cd message-handler
#./create_docker_image.sh
#cd ..

#kubectl apply -f ./message-handler/deployment.yaml
#sleep 1
#kubectl apply -f ./message-handler/service.yaml
sleep 1

minikube service list
