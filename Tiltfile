docker_build("coacher", "app")
docker_build("coacher-nginx", "app", dockerfile="app/Dockerfile.nginx")
k8s_yaml(kustomize('.'))
k8s_resource(
  workload='coacher',
  port_forwards=['8000:8000', '8080:8080']
)