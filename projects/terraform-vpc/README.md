# Multi-AZ VPC with Terraform

Creates a VPC, public and private subnets across two availability zones, an internet gateway, and route tables. NAT gateways are omitted to keep the example cost-conscious; add them if private subnets need outbound internet access.

```bash
terraform init
terraform plan
terraform apply
```

Requires Terraform and AWS credentials. Review the plan and expected AWS charges before applying. Run `terraform destroy` when finished.
