# Azure Logic App - Customer Pipeline Alerts

## Purpose
This Logic App is responsible for sending automated email notifications whenever the Customer Data Pipeline fails.

## Trigger
- HTTP Request Trigger
- Invoked from Synapse Monitoring Pipeline (`pl_monitor_customer_pipeline`)

## Workflow

Synapse Monitoring Pipeline
        ↓
HTTP POST Request
        ↓
Azure Logic App
        ↓
Gmail Connector
        ↓
Failure Email Notification

## Request Payload

```json
{
  "pipeline_name": "pl_customer_landing_to_bronze",
  "run_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "status": "Failed",
  "start_time": "2026-07-13 09:15:20",
  "end_time": "2026-07-13 09:18:42",
  "error_message": "Sample error message"
}
```

## Email Contents

- Pipeline Name
- Run ID
- Pipeline Status
- Start Time
- End Time
- Error Message

## Features

- Automatic email alerts
- HTTP-triggered workflow
- Gmail integration
- Supports real-time pipeline failure notifications
- Easily extensible for Microsoft Teams, Slack, or SMS alerts

## Azure Services Used

- Azure Logic Apps (Consumption)
- Gmail Connector
- Azure Synapse Analytics

## Future Enhancements

- Success notifications
- Daily pipeline summary
- Teams integration
- Retry mechanism
- Multiple recipient groups
- Severity-based alerts
