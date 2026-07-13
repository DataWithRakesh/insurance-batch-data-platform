# Deployment Guide - Customer Pipeline Alert Logic App

This document describes how to deploy the Azure Logic App used for Customer Pipeline Failure Notifications.

---

# Prerequisites

- Azure Subscription
- Resource Group
- Azure Logic Apps (Consumption)
- Gmail or Outlook Account
- Azure Synapse Analytics Workspace

---

# Step 1 - Deploy Logic App

1. Open Azure Portal.
2. Search **Deploy a custom template**.
3. Click **Build your own template in the editor**.
4. Upload the file:

```
la_customer_pipeline_alert.json
```

5. Click **Save**.
6. Provide the following details:

- Subscription
- Resource Group
- Logic App Name
- Region

7. Click **Review + Create**.
8. Click **Create**.

---

# Step 2 - Configure Email Connector

1. Open the deployed Logic App.
2. Navigate to **Logic App Designer**.
3. Open the Gmail (or Outlook) action.
4. Authenticate using your email account.
5. Publish the Logic App.

> Note:
> Email credentials are not stored in GitHub and must be configured after deployment.

---

# Step 3 - Generate HTTP Endpoint

1. Open the **When an HTTP request is received** trigger.
2. Copy the generated **HTTP POST URL**.

Example:

```
https://prod-xx.logic.azure.com/workflows/...
```

---

# Step 4 - Configure Synapse Monitoring Pipeline

Open the Synapse Monitoring Pipeline.

Activity:

```
web_send_email_alert
```

Update:

- URL → Paste the generated HTTP POST URL.
- Method → POST

Headers

```json
{
    "Content-Type": "application/json"
}
```

Body

```json
{
    "pipeline_name":"@{activity('lk_latest_pipeline_run').output.firstRow.pipeline_name}",
    "run_id":"@{activity('lk_latest_pipeline_run').output.firstRow.run_id}",
    "status":"@{activity('lk_latest_pipeline_run').output.firstRow.status}",
    "start_time":"@{activity('lk_latest_pipeline_run').output.firstRow.start_time}",
    "end_time":"@{activity('lk_latest_pipeline_run').output.firstRow.end_time}",
    "error_message":"@{activity('lk_latest_pipeline_run').output.firstRow.error_message}"
}
```

---

# Step 5 - Validate

Update the latest pipeline status to **Failed**.

Execute:

```
pl_monitor_customer_pipeline
```

Expected Flow

```
Lookup
      │
      ▼
If Condition
      │
      ▼
Web Activity
      │
      ▼
Azure Logic App
      │
      ▼
Gmail
      │
      ▼
Failure Email
```

Verify that the email contains:

- Pipeline Name
- Run ID
- Pipeline Status
- Start Time
- End Time
- Error Message

---

# Azure Services Used

- Azure Synapse Analytics
- Azure Logic Apps (Consumption)
- Azure SQL Database
- Gmail Connector

---

# Repository Structure

```
logicapp/
│
├── la_customer_pipeline_alert.json
├── README.md
└── deployment.md
```

---

# Notes

- Gmail/Outlook credentials are **not** included in the exported Logic App template.
- The HTTP callback URL is generated after deployment and must be updated in the Synapse Web Activity.
- Store secrets securely (for example, in Azure Key Vault) in production environments instead of embedding them in workflows.
