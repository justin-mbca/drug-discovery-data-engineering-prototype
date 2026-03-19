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

---

For more details, see the main [README.md](README.md) and [infra/](infra/) directory.
