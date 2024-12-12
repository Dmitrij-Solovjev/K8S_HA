#!/bin/bash

###Install the RabbitMQ operator 
kubectl apply -f https://github.com/rabbitmq/cluster-operator/releases/latest/download/cluster-operator.yml
sleep 1

###Check if the components are healthy in the rabbitmq-system namespace
kubectl get all -o wide -n rabbitmq-system

kubectl apply -f rabbitmqcluster.yaml
sleep 1

minikube service list
