# Kubernetes Application and Database

Local demo with Kubernetes manifests for a web app and PostgreSQL. Build the sample app image and load it into your cluster, then apply `k8s/`. The demo credentials are placeholders; use Kubernetes Secrets backed by an external secret manager for real deployments. A single PostgreSQL replica is for demonstration, not production high availability.

```bash
docker build -t cloud-demo-app:local .
# For kind: kind load docker-image cloud-demo-app:local
kubectl apply -f k8s/
kubectl get pods,svc
```
