# Terraform for React Frontend GCS Hosting

resource "google_storage_bucket" "frontend" {
  name          = "${var.project_id}-frontend"
  location      = "US"
  force_destroy = true
  website {
    main_page_suffix = "index.html"
    not_found_page   = "404.html"
  }
  uniform_bucket_level_access = true
}

resource "google_storage_bucket_iam_binding" "public" {
  bucket = google_storage_bucket.frontend.name
  role   = "roles/storage.objectViewer"
  members = [
    "allUsers",
  ]
}

output "frontend_gcs_url" {
  value = "https://storage.googleapis.com/${google_storage_bucket.frontend.name}/index.html"
}
