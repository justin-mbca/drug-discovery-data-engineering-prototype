# Infrastructure as Code with Terraform and GCP

## Prototype Component → Terraform Resource Mapping

| Prototype Component         | GCP Service / Resource         | Terraform Resource Type                | Purpose / Example Usage                                 |
|----------------------------|-------------------------------|----------------------------------------|--------------------------------------------------------|
| FastAPI Backend            | Cloud Run / GKE / VM          | `google_cloud_run_service` / `google_container_cluster` / `google_compute_instance` | Deploys your API as a managed service or container     |
| ETL/Analytics (Python)     | BigQuery                      | `google_bigquery_dataset`, `google_bigquery_table`      | Stores and queries processed data                      |
| Mock/Raw Data Storage      | Cloud Storage (GCS)           | `google_storage_bucket`                | Stores raw files, ETL staging, or static assets        |
| Service Account            | IAM Service Account           | `google_service_account`               | Secure identity for backend/ETL to access GCP APIs     |
| Permissions                | IAM Roles/Bindings            | `google_project_iam_member`            | Grants BigQuery, GCS, or other access to service acct  |
| Secrets (API keys, etc.)   | Secret Manager                | `google_secret_manager_secret`         | Securely stores credentials for backend/ETL            |
| Networking/Security        | VPC, Firewall, Calico (GKE)   | `google_compute_network`, `google_compute_firewall`, GKE network config | Secure, private communication between services         |
| Frontend (React)           | GCS Website / Vercel          | `google_storage_bucket` (website)      | Optionally host static frontend on GCS                 |

---

## Example: Minimal Terraform for BigQuery + Service Account

```hcl
provider "google" {
  project = "your-gcp-project"
  region  = "us-central1"
}

resource "google_bigquery_dataset" "etl" {
  dataset_id = "etl_data"
  location   = "US"
}

resource "google_bigquery_table" "compounds" {
  dataset_id = google_bigquery_dataset.etl.dataset_id
  table_id   = "compounds"
  schema     = file("schemas/compounds.json")
}

resource "google_service_account" "backend" {
  account_id   = "backend-service"
  display_name = "Backend Service Account"
}

resource "google_project_iam_member" "bq_access" {
  project = "your-gcp-project"
  role    = "roles/bigquery.dataEditor"
  member  = "serviceAccount:${google_service_account.backend.email}"
}
```

---

## How Terraform Links GCP Services and Drives the Workflow

- **Declarative Infrastructure:** You describe your desired GCP resources (datasets, tables, service accounts, etc.) in Terraform configuration files.
- **Automated Provisioning:** Running `terraform apply` creates or updates all resources in GCP to match your configuration, eliminating manual setup.
- **Resource Linking:** Terraform automatically links resources (e.g., a service account is granted IAM permissions to access BigQuery) using references in the config.
- **Reproducibility:** The same Terraform code can be used to recreate the environment in any GCP project or region, ensuring consistency.
- **Change Management:** Changes to infrastructure are tracked in version control and applied incrementally, making updates safe and auditable.
- **Integration with Prototype:**
  - Your backend and ETL code use the service account credentials and resource names provisioned by Terraform.
  - Data flows from APIs or ETL jobs into BigQuery tables and GCS buckets created by Terraform.
  - All infrastructure dependencies are managed as code, so onboarding, scaling, or disaster recovery is fast and reliable.

---

For more details, see the [Terraform documentation](https://www.terraform.io/docs/providers/google/index.html) and [GCP resource docs](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/).
