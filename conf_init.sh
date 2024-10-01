#!/bin/bash

echo "Initializing GCP project $GCP_PROJECT_ID and setting up environment..."
 
gcloud projects describe $GCP_PROJECT_ID
