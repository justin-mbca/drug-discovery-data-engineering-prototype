#!/bin/bash
# Automated GCP React frontend build and deploy script
set -e

# Set your API URL for production
export REACT_APP_API_URL="https://backend-871527614878.us-central1.run.app"

cd "$(dirname "$0")/frontend"

echo "Building React app with API URL: $REACT_APP_API_URL"
npm install
npm run build

BUCKET_NAME="my-fastapi-demo-490623-frontend"

# Check if bucket exists
if ! gsutil ls -b gs://$BUCKET_NAME > /dev/null 2>&1; then
  echo "GCS bucket $BUCKET_NAME does not exist. Please run Terraform first."
  exit 1
fi

echo "Uploading build output to GCS bucket: $BUCKET_NAME"
gsutil -m rsync -r build gs://$BUCKET_NAME

echo "Deployment complete."
echo "Access your site at: https://storage.googleapis.com/$BUCKET_NAME/index.html"
