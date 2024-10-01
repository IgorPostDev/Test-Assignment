# GCP Project Setup and Deployment

## Overview

This project automates the creation of a new environment in GCP with necessary secrets and variables, and deploys the application to Google Cloud Run.

## Usage

### 1. Setting up a New GCP Environment

1. **Clone the repository** and configure the following GitHub Secrets:
   - `GCP_SERVICE_ACCOUNT_KEY`: JSON key for the service account used for GCP authentication.

2. **Go to the Actions tab** and run the **Configure GCP Environment** workflow with the following parameters:
   - `environment_name`: The name of the environment (e.g., `staging` or `production`).
   - `gcp_project_id`: The ID of the GCP project.

3. Once the GitHub Action is complete, it will set up the environment and create the secrets needed for the deployment.

### 2. Deploying the Application to Google Cloud Run

1. **Go to the Actions tab** and run the **Deploy to Cloud Run** workflow with the following parameter:
   - `environment_name`: The name of the environment created in the first step.

2. The GitHub Action will deploy the application to Google Cloud Run using the specified environment.

### 3. Setting up Triggers

1. **To configure triggers**, such as Google Cloud Scheduler, run the following command:
   ```bash
   ./conf_triggers.sh
