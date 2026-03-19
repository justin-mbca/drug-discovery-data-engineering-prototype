# Cloud Run build, push, and deploy
REGION=us-central1
PROJECT_ID=my-fastapi-demo-490623
REPO=backend-repo
IMAGE=backend
TAG=latest
SERVICE_NAME=mock-apis
IMAGE_URI=$(REGION)-docker.pkg.dev/$(PROJECT_ID)/$(REPO)/$(IMAGE):$(TAG)

.PHONY: cloudrun-build cloudrun-push cloudrun-deploy cloudrun-all


cloudrun-build:
	docker build -t $(IMAGE_URI) .


cloudrun-push:
	gcloud auth configure-docker $(REGION)-docker.pkg.dev --quiet
	gcloud builds submit --tag $(IMAGE_URI) .

cloudrun-deploy:
	gcloud run deploy $(SERVICE_NAME) \
	  --image=$(IMAGE_URI) \
	  --platform=managed \
	  --region=$(REGION) \
	  --allow-unauthenticated \
	  --project=$(PROJECT_ID)

cloudrun-all: cloudrun-build cloudrun-push cloudrun-deploy

# Usage:
#   cd backend
#   make cloudrun-all
#
# After deployment, Cloud Run will output a public URL. All mock APIs will be available at:
#   <URL>/benchling/data
#   <URL>/cdd/data
#   <URL>/mosaic/data
# Makefile for FastAPI Backend Docker Builds

# Local build (Apple Silicon/ARM64)
local-build:
	docker build -t fastapi-backend:local .

# Cloud build (GKE/AMD64)
gke-build:
	docker buildx build --platform linux/amd64 -t fastapi-backend:latest .
	docker tag fastapi-backend:latest gcr.io/my-fastapi-demo-490623/fastapi-backend:latest
	docker push gcr.io/my-fastapi-demo-490623/fastapi-backend:latest

# Restart GKE deployment after push
gke-restart:
	kubectl rollout restart deployment fastapi-backend
