# Serverless AI Content API

Reference architecture: API Gateway → Lambda → Amazon Bedrock, with DynamoDB persistence. Amplify can host a frontend that calls the API.

## Contents

- `handler.py`: Python Lambda handler. Uses Bedrock Runtime and DynamoDB via boto3.
- `template.yaml`: AWS SAM template for the REST API, Lambda, and table.

## Deploy

Install and configure AWS CLI, AWS SAM CLI, and credentials in an AWS account. Ensure Bedrock model access is enabled in your region. From this directory:

```bash
sam build
sam deploy --guided
```

Send a POST with JSON `{"prompt":"Write a short welcome message"}` to the printed API URL. Model availability and access vary by AWS account and region. Do not put credentials in source control.
