resource "google_bigquery_table" "benchling" {
  dataset_id = google_bigquery_dataset.drug_discovery.dataset_id
  table_id   = "benchling"
  schema     = <<EOF
[
  {"name": "entry_id", "type": "STRING", "mode": "REQUIRED"},
  {"name": "experiment", "type": "STRING", "mode": "NULLABLE"},
  {"name": "date", "type": "STRING", "mode": "NULLABLE"},
  {"name": "scientist", "type": "STRING", "mode": "NULLABLE"},
  {"name": "result", "type": "STRING", "mode": "NULLABLE"}
]
EOF
}

resource "google_bigquery_table" "cdd" {
  dataset_id = google_bigquery_dataset.drug_discovery.dataset_id
  table_id   = "cdd"
  schema     = <<EOF
[
  {"name": "compound_id", "type": "STRING", "mode": "REQUIRED"},
  {"name": "name", "type": "STRING", "mode": "NULLABLE"},
  {"name": "structure", "type": "STRING", "mode": "NULLABLE"},
  {"name": "activity", "type": "STRING", "mode": "NULLABLE"},
  {"name": "project", "type": "STRING", "mode": "NULLABLE"}
]
EOF
}

resource "google_bigquery_table" "mosaic" {
  dataset_id = google_bigquery_dataset.drug_discovery.dataset_id
  table_id   = "mosaic"
  schema     = <<EOF
[
  {"name": "sample_id", "type": "STRING", "mode": "REQUIRED"},
  {"name": "location", "type": "STRING", "mode": "NULLABLE"},
  {"name": "quantity", "type": "INTEGER", "mode": "NULLABLE"},
  {"name": "unit", "type": "STRING", "mode": "NULLABLE"},
  {"name": "status", "type": "STRING", "mode": "NULLABLE"}
]
EOF
}
