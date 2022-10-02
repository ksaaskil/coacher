# Coacher

Coacher helps you focus on what matters.

## User stories

- I want to configure Coacher to send my team a weekly Slack reminder to remind us about our values
- I want to configure Coacher to send me a mobile notification every two weeks to remind myself about my values

## Development

Install [Tilt](https://docs.tilt.dev/index.html) and [Kustomize](https://kubectl.docs.kubernetes.io/installation/kustomize/).

[Create a local development cluster](https://docs.tilt.dev/choosing_clusters.html).

> For Minikube:
> ```bash
> minikube start
> eval $(minikube docker-env)
> ```

Start Tilt:

```bash
tilt up
```

Once the stack is up, make a test request:

```bash
curl http://localhost:8000/reminders/debug
```

With the returned task ID, request the async result:

```bash
curl http://localhost:8000/reminders/debug/<TASK_ID>
```

## TO DO

- [x] Setup Celery
- [] Setup GitHub workflows
- [] Setup first example notificaiton

## Resources

- [Scaling Celery workers with RabbitMQ on Kubernetes](https://learnk8s.io/scaling-celery-rabbitmq-kubernetes)
