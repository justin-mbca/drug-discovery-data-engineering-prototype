# Drug Discovery Data Engineering Prototype: Deployment & Automation Summary

## Overview
This project demonstrates a full-stack, cloud-native data engineering pipeline for drug discovery, integrating mock APIs, automated data loading, and cloud infrastructure as code.

---

## Architecture
- **Backend:** FastAPI (Python) mock APIs for Benchling, CDD, Mosaic
- **Frontend:** React (Vercel deployment)
- **Data Warehouse:** Google BigQuery
- **Infrastructure:** Terraform (GCP resources, BigQuery dataset/tables)
- **Automation:** Loader script for batch data ingestion
- **CI/CD:** GitHub Actions, Docker, Cloud Run

---

## Key Steps Completed

### 1. Cloud Infrastructure
- Provisioned GCP project: `my-fastapi-demo-490623`
- Created BigQuery dataset: `drug_discovery` (location: US)
- Created tables: `benchling`, `cdd`, `mosaic` with appropriate schemas
- All infrastructure managed via Terraform (`infra/`)

### 2. Backend & API
- FastAPI backend with endpoints:
  - `/benchling/data`
  - `/cdd/data`
  - `/mosaic/data`
- Deployed to Cloud Run: [Cloud Run Service URL](https://backend-871527614878.us-central1.run.app)
- Endpoints return paginated mock data for batch loading

### 3. Frontend
- React app deployed to Vercel: [Vercel Frontend URL](https://drug-discovery-frontend.vercel.app) *(replace with actual URL)*

### 4. Data Loader Automation
- Python script (`backend/scripts/load_mocked_to_bq.py`) fetches data from each API and loads into BigQuery
- Automation script (`run_all_loaders.sh`) runs all loaders with correct environment variables
- Loader deduplicates by unique ID per table
- Loader can be run manually or scheduled in CI/CD

### 5. Testing & Validation
- Automated endpoint tests (pytest) for pagination and data structure
- Manual and automated verification of data in BigQuery

---

## How to Reproduce
1. **Provision GCP resources:**
   ```sh
   cd infra
   terraform apply -auto-approve -var="project_id=my-fastapi-demo-490623"
   ```
2. **Deploy backend:**
   ```sh
   cd backend
   make cloudrun-all
   ```
3. **Deploy frontend:**
   - Push to GitHub, Vercel auto-deploys
4. **Run loader:**
   ```sh
   bash run_all_loaders.sh
   ```
5. **Verify:**
   - BigQuery Console: [BigQuery Console](https://console.cloud.google.com/bigquery?project=my-fastapi-demo-490623)
   - Cloud Run: [Cloud Run Service](https://backend-871527614878.us-central1.run.app)
   - Frontend: [Vercel Frontend](https://drug-discovery-frontend.vercel.app)

---

## URLs to Share
- **GCP BigQuery Console:** https://console.cloud.google.com/bigquery?project=my-fastapi-demo-490623
- **Cloud Run Backend:** https://backend-871527614878.us-central1.run.app
- **Vercel Frontend:** https://drug-discovery-frontend.vercel.app *(replace with actual URL if different)*

---

## Notes
- All code, infra, and automation are in this repository.
- For full batch loading, update loader to iterate all pages.
- Contact: justin@example.com *(replace with your email)*
