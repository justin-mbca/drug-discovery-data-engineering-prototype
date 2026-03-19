# Drug Discovery Data Engineering Prototype: Deployment Overview

## Project Structure
- **Backend:** FastAPI (Python), containerized with Docker
- **Frontend:** React, containerized with Docker
- **Infrastructure as Code:** Terraform for GCP resources

## Deployment Strategies Demonstrated

### 1. Google Cloud Run (Serverless Backend)
- **Backend** deployed as a Docker container to Cloud Run
- **Image** built locally and pushed to Google Artifact Registry
- **Public endpoint** with secure HTTPS
- **Cost-optimized:** Scales to zero, pay-per-use
- **Deployment Steps:**
  - Docker build/tag/push
  - gcloud run deploy with --allow-unauthenticated

### 2. Vercel (Frontend Demo)
- **Frontend** deployed to Vercel for rapid, serverless hosting
- **Public URL** for easy sharing and demo

### 3. Google Kubernetes Engine (GKE, Advanced Option)
- **Both frontend and backend** can be deployed as Kubernetes Deployments
- **Services** expose each app internally
- **GKE Ingress** provides public endpoints for both frontend and backend
- **Autopilot mode** for cost-effective, managed Kubernetes
- **Deployment Steps:**
  - kubectl apply -f <manifest>.yaml for each component
  - Ingress for unified public access

### 4. Terraform Automation
- **Terraform** provisions GCP resources: BigQuery, GCS, Service Account, Cloud Run
- **Infrastructure as Code**: Reproducible, version-controlled cloud setup
- **Cloud Run deployment** can be automated by uncommenting and configuring the resource in terraform/main.tf

## Security & Access
- **Cloud Run**: Can be public or restricted with IAM
- **GKE**: Ingress allows fine-grained access control
- **IAM roles**: Principle of least privilege for service accounts and users

## Cost Optimization
- **Cloud Run**: No cost when idle, scales with demand
- **GKE Autopilot**: Pay only for pod resources, no cluster management fee
- **Terraform**: Provisions only free-tier or minimal resources for demo

## How to Demo
- Share public URLs for both frontend (Vercel or GKE Ingress) and backend (Cloud Run or GKE Ingress)
- Show Terraform code for infrastructure automation
- Explain Docker and Kubernetes manifests for advanced deployment

---

**This project demonstrates modern, cloud-native, and cost-effective deployment strategies suitable for production and rapid prototyping.**
