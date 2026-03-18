# drug-discovery-data-engineering-prototype

## Description
A full-stack prototype for a Drug Discovery Data Engineering platform, closely aligned with the Calico Senior Data Engineer JD. This project demonstrates:
- End-to-end data flow from laboratory informatics systems (mocked CDD Vault, Mosaic, Benchling) to a cloud data warehouse (GCP BigQuery)
- A Python FastAPI backend for data integration and API exposure
- A React frontend for data visualization and review
- Infrastructure-as-code with Terraform for GCP resource provisioning
- Containerization with Docker and CI/CD readiness

## Architecture
```mermaid
graph TD
    subgraph Frontend
        FE[React App]
    end
    subgraph Backend
        BE[FastAPI]
        CDD[CDD Vault Client (Mock)]
        MOS[Mosaic Client (Mock)]
        BEN[Benchling Client (Mock)]
        BQUTIL[BigQuery Client]
    end
    subgraph GCP
        BQ[BigQuery Dataset]
    end
    FE -- REST API --> BE
    BE -- REST API --> CDD
    BE -- REST API --> MOS
    BE -- REST API --> BEN
    BE -- Query --> BQUTIL
    BQUTIL -- API --> BQ
```

## Setup Instructions
### Prerequisites
- Docker
- Google Cloud account with BigQuery enabled
- (Optional) Node.js and Python 3.10+ for local development

### 1. Infrastructure (Terraform)
```
cd infra
terraform init
terraform apply -var="project_id=YOUR_GCP_PROJECT_ID"
```

### 2. Backend (FastAPI)
```
cd backend
docker build -t drug-backend .
# Mount GCP credentials and set env var:
docker run -p 8000:8000 \
  -v $HOME/.config/gcloud/application_default_credentials.json:/app/application_default_credentials.json \
  -e GOOGLE_APPLICATION_CREDENTIALS=/app/application_default_credentials.json \
  drug-backend
```

### 3. Frontend (React)
```
cd frontend
docker build -t drug-frontend .
docker run -p 3000:3000 drug-frontend
```

### 4. Access the App
- Open http://localhost:3000
- The frontend displays data from CDD Vault, Mosaic, Benchling (mocked), and real BigQuery tables

## Usage
- The backend exposes endpoints for each data source and `/bigquery/data` for live BigQuery data
- The frontend fetches and displays all data sources
- Easily extend to real APIs by replacing mock clients

## Alignment with Calico JD
- **End-to-End Project Ownership:** Demonstrates requirements gathering, integration, and deployment
- **System Integration:** Connects multiple informatics systems and GCP BigQuery
- **Data Flow Architecture:** Shows seamless data movement and review
- **Full-Stack Tool Development:** Combines Python (FastAPI) and React
- **Engineering Excellence:** Uses Docker, Terraform, and best practices for CI/CD
- **Mentorship & Leadership:** Code is modular, documented, and ready for team onboarding

---

> For questions or demo, contact the project author.
