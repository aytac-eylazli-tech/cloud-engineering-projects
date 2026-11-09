# Centralized Monitoring and Alerts

Example CloudWatch alarm and SNS notification path. To connect PagerDuty, create an Events API v2 integration and store its integration URL as a Secrets Manager secret; do not commit it.

Deploy the alarm after replacing the example metric dimensions and topic email. Confirm the SNS subscription from the inbox. For PagerDuty, route SNS through a small Lambda forwarder that reads the URL from Secrets Manager, or use PagerDuty's supported AWS integration for your account.
