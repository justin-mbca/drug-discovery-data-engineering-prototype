# Setup Guide: Drug Discovery Data Engineering Prototype

This guide provides step-by-step instructions and commands for setting up the project locally and on Google Cloud Platform (GCP).

---

## 1. GCP Project Setup

```sh
gcloud projects create YOUR_PROJECT_ID --name="Your Project Name"
gcloud config set project YOUR_PROJECT_ID
gcloud beta billing projects link YOUR_PROJECT_ID --billing-account=BILLING_ACCOUNT_ID
gcloud services enable bigquery.googleapis.com storage.googleapis.com run.googleapis.com cloudbuild.googleapis.com iam.googleapis.com
```

## 2. IAM Role Configuration

```sh
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID --member="user:your.email@example.com" --role="roles/bigquery.admin"
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID --member="user:your.email@example.com" --role="roles/storage.admin"
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID --member="user:your.email@example.com" --role="roles/run.admin"
```

## 3. Infrastructure Provisioning (Terraform)

```sh
cd infra
terraform init
terraform apply -var="project_id=YOUR_PROJECT_ID"
```

## 4. Local Development

```sh
# Frontend
cd frontend
REACT_APP_API_URL=http://localhost:8000 npm install
npm start

# Backend
cd backend
uvicorn main:app --reload
```

## 5. Docker Build & Run (Local)

```sh
# Backend
cd backend
docker build -t fastapi-backend:local .
docker run -p 8000:8000 fastapi-backend:local

# Frontend
cd frontend
docker build -t react-frontend:local .
docker run -p 3000:3000 react-frontend:local
```

## 6. BigQuery Table Creation

```sh
cd backend/scripts
python create_bq_tables.py
```

## 7. Deploy Backend to Cloud Run

```sh
cd backend
docker build -t gcr.io/YOUR_PROJECT_ID/backend:latest .
docker push gcr.io/YOUR_PROJECT_ID/backend:latest
gcloud run deploy backend --image gcr.io/YOUR_PROJECT_ID/backend:latest --region us-central1 --platform managed --allow-unauthenticated
```

## 8. Deploy Frontend to GCS

```sh
cd frontend
npm run build
gsutil -m rsync -r build gs://YOUR_GCS_BUCKET_NAME
gsutil iam ch allUsers:objectViewer gs://YOUR_GCS_BUCKET_NAME
```

## 9. Deploying with Kubernetes (GKE)

```sh
# Build and push backend Docker image for GKE
cd backend
docker buildx build --platform linux/amd64 -t fastapi-backend:latest .
docker tag fastapi-backend:latest gcr.io/YOUR_PROJECT_ID/fastapi-backend:latest
docker push gcr.io/YOUR_PROJECT_ID/fastapi-backend:latest

# Build and push frontend Docker image for GKE
cd ../frontend
docker buildx build --platform linux/amd64 -t react-frontend:latest .
docker tag react-frontend:latest gcr.io/YOUR_PROJECT_ID/react-frontend:latest
docker push gcr.io/YOUR_PROJECT_ID/react-frontend:latest

# Apply Kubernetes manifests (from infra/)
cd ../infra
kubectl apply -f backend-deployment.yaml
kubectl apply -f backend-service.yaml
kubectl apply -f frontend-deployment.yaml
kubectl apply -f frontend-service.yaml
kubectl apply -f ingress.yaml

# Restart deployments after pushing new images
kubectl rollout restart deployment fastapi-backend
kubectl rollout restart deployment react-frontend
```

## Deployment Options: When to Use Each

| Method                | Use When...                                                                 |
|-----------------------|------------------------------------------------------------------------------|
| **GCS (Frontend only)** | You want simple, cost-effective static hosting for the React frontend only.  |
| **Cloud Run (Backend)** | You need to deploy a containerized backend API with minimal infrastructure management and autoscaling. |
| **Kubernetes (GKE)**    | You require full control, advanced orchestration, multi-service deployments, or production-grade scalability and reliability for both frontend and backend. |

- **GCS** is best for static sites with no server-side logic.
- **Cloud Run** is ideal for quick, serverless backend deployments with autoscaling.
- **Kubernetes** is recommended for complex, multi-service, or production environments where you need advanced features and control.

---

For more details, see the main [README.md](README.md) and [infra/](infra/) directory.
