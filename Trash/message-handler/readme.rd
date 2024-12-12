# Сервис, взаимодействующий через последовательный порт с радиомодулем, отправляющий и принимающий сообщения

# Запуск
minikube start
kubectl delete all --all

docker build --no-cache . -t flask-hello-world-image:latest
docker image save -o image.tar flask-hello-world-image:latest
minikube image load image.tar

kubectl apply -f deploy.yaml
kubectl apply -f app-service.yaml

kubectl get all

minikube service list                        # для получения ссылки (ip + port)

#minikube service hello-kubernetes-svc --url # В этой команде нет необходимости
