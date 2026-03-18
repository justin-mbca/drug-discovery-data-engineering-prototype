provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_bigquery_dataset" "drug_discovery" {
  dataset_id = "drug_discovery"
  location   = var.region
}
