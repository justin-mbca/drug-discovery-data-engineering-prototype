# Minimal, Cost-Optimized Terraform for GCP Data Engineering Prototype

# This configuration provisions:
# - A BigQuery dataset and table (free tier)
# - A Cloud Storage bucket (free tier)
# - A service account with BigQuery and GCS access (free)
# - (Optionally) Cloud Run for backend (free tier)

provider "google" {
  project = var.project_id
  region  = var.region
}

variable "project_id" {}
variable "region" { default = "us-central1" }

# BigQuery Dataset
resource "google_bigquery_dataset" "etl" {
  dataset_id = "etl_data"
  location   = "US"
}

# BigQuery Table (example schema)
resource "google_bigquery_table" "compounds" {
  dataset_id = google_bigquery_dataset.etl.dataset_id
  table_id   = "compounds"
  schema     = file("schemas/compounds.json")
}

# Cloud Storage Bucket
resource "google_storage_bucket" "etl_data" {
  name     = "${var.project_id}-etl-data-demo"
  location = var.region
  force_destroy = true
}

# Service Account
resource "google_service_account" "backend" {
  account_id   = "backend-service"
  display_name = "Backend Service Account"
}

# IAM: Service Account can access BigQuery and GCS
resource "google_project_iam_member" "bq_access" {
  project = var.project_id
  role    = "roles/bigquery.dataEditor"
  member  = "serviceAccount:${google_service_account.backend.email}"
}

resource "google_project_iam_member" "gcs_access" {
  project = var.project_id
  role    = "roles/storage.objectAdmin"
  member  = "serviceAccount:${google_service_account.backend.email}"
}

resource "google_cloud_run_service" "backend" {
  name     = "fastapi-backend-demo"
  location = var.region
  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/fastapi-backend:latest"
      }
      service_account_name = google_service_account.backend.email
    }
  }
  traffic {
    percent         = 100
    latest_revision = true
  }
  autogenerate_revision_name = true
}

output "bigquery_dataset_id" {
  value = google_bigquery_dataset.etl.dataset_id
}

output "gcs_bucket_name" {
  value = google_storage_bucket.etl_data.name
}

output "service_account_email" {
  value = google_service_account.backend.email
}
