# Cloud Engineering Projects

Portfolio examples for AWS, Terraform, CI/CD, observability, and Kubernetes. Each folder is an independent project. The examples are intentionally small and meant to be extended; cloud deployment requires your own accounts and credentials.

## Projects

1. [Serverless AI Content API](projects/serverless-ai) — API Gateway, Lambda, DynamoDB, Bedrock, Amplify.
2. [Centralized Monitoring and Alerts](projects/monitoring-alerts) — CloudWatch, SNS, PagerDuty.
3. [Multi-AZ VPC with Terraform](projects/terraform-vpc) — reusable AWS network infrastructure.
4. [CI/CD Pipeline](projects/ci-cd-pipeline) — GitHub Actions and AWS CodePipeline examples.
5. [Kubernetes App and Database](projects/kubernetes-app) — Deployment, Service, PostgreSQL, and persistence.

## Publish to GitHub

Create an empty repository on GitHub, then from this directory run:

```bash
git init
git add .
git commit -m "Add cloud engineering portfolio projects"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/cloud-engineering-projects.git
git push -u origin main
```

Replace `YOUR_USERNAME` and the repository path. Never commit AWS keys, PagerDuty tokens, `.env` files, Terraform state, or kubeconfig files. See each project README for prerequisites and deployment notes.
