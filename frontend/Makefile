# Makefile for React Frontend Docker Builds

# Local build (Apple Silicon/ARM64)
local-build:
	docker build -t react-frontend:local .

# Cloud build (GKE/AMD64)
gke-build:
	docker buildx build --platform linux/amd64 -t react-frontend:latest .
	docker tag react-frontend:latest gcr.io/my-fastapi-demo-490623/react-frontend:latest
	docker push gcr.io/my-fastapi-demo-490623/react-frontend:latest

# Restart GKE deployment after push
gke-restart:
	kubectl rollout restart deployment react-frontend
