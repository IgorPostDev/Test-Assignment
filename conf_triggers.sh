#!/bin/bash

gcloud scheduler jobs create http scheduler-job \
  --schedule="*/5 * * * *" \
  --http-method=POST \
  --uri=https://<YOUR_CLOUD_RUN_URL>/scheduler \
  --headers="Content-Type=application/json" \
  --message-body='{"data": "scheduler payload"}' \
  --time-zone="UTC"
