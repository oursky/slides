# Redis HA Example

## Cloud Pirates Chart
1. Copy [redis chart](https://github.com/CloudPirates-io/helm-charts/tree/main/charts/redis) to `charts/redis-cloudpirates/`.
2. `helm dependency update && helm dependency build`.

## Deploy
```
kubectl create ns redis-ha-example
helm upgrade --install -n redis-ha-example redis .
kubectl -n redis-ha-example get pod

helm uninstall -n redis-ha-example redis
```
