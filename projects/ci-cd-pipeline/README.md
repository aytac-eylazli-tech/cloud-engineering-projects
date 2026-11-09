# CI/CD Pipeline

Includes a GitHub Actions workflow for build/test/deploy and a minimal CodePipeline CloudFormation skeleton. Configure AWS OIDC instead of long-lived access keys: add a GitHub Actions IAM role and set repository variable `AWS_ROLE_ARN` and secret `AWS_REGION`. Update the deploy command for your app. The workflow deliberately does not deploy until you provide a real build artifact and deployment target.
