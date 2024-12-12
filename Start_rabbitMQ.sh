#!/bin/bash

###Install the RabbitMQ operator 
#kubectl apply -f https://github.com/rabbitmq/cluster-operator/releases/latest/download/cluster-operator.yml
#sleep 1

###Check if the components are healthy in the rabbitmq-system namespace
#kubectl get all -o wide -n rabbitmq-system

#kubectl apply -f rabbitmqcluster.yaml
#sleep 1

# Последний тест
kubectl delete all --all

kubectl apply -f https://github.com/rabbitmq/cluster-operator/releases/latest/download/cluster-operator.yml
sleep 1
kubectl apply -f https://raw.githubusercontent.com/rabbitmq/cluster-operator/main/docs/examples/hello-world/rabbitmq.yaml
sleep 1
# Согласно документации должно работать, хоть и нет портов наружу как в верхнем.
# Для получения доступа к админке используйте
#username="$(kubectl get secret hello-world-default-user -o jsonpath='{.data.username}' | base64 --decode)"
#echo "username: $username"
#password="$(kubectl get secret hello-world-default-user -o jsonpath='{.data.password}' | base64 --decode)"
#echo "password: $password"
#kubectl port-forward "service/hello-world" 15672





minikube service list
