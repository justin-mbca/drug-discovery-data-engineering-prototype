output "benchling_table_id" {
  value = google_bigquery_table.benchling.table_id
}

output "cdd_table_id" {
  value = google_bigquery_table.cdd.table_id
}

output "mosaic_table_id" {
  value = google_bigquery_table.mosaic.table_id
}
output "bigquery_dataset_id" {
  value = google_bigquery_dataset.drug_discovery.dataset_id
}
