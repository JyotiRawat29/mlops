Deploying Model into Production
docker build -t ml_opsapp .
docker run -p 50001:5001 ml_opsapp
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"features":[3.25960000e+00,  3.30000000e+01,  5.01765650e+00,
         1.00642055e+00,  2.30000000e+03,  3.69181380e+00,
         3.27100000e+01, -1.17030000e+02]}'
Install minikube (brew install kubectl-cli)
eval $(minikube docker-env)
docker build -t ml_opsapp:latest
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
minikube service ml-model-service --url
curl -X POST https://127.0.0.1:62316/predict -H "Content-Type: application/json" -d '{"features":[8,41,61]}'


#podman cnatiner inspect
"IPAddress": "10.88.0.16

Excercise:

Create a hello world webpage from any language / framework you want
Create a docker image from it
Start a Kubernetes cluster from a cloud provider ( it will be easier to setup and troubleshoot than a local one, so you can focus on deploying on Kubernetes first only )
Create a Deployment for it : try to see if pod start
Create a Service for it : try to access it from an another pod in the cluster (ex: netshoot)
Create a Volume for it : put some data in a volume, and try to access it from the pod itself
Deploy Nginx Ingress Controller with Helm
Create an Ingress for the hello world service, and try to access your hello world webpage from outside

