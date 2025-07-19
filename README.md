
# Event-Driven Data Pipeline using AWS Lambda, S3, API Gateway, and Terraform

This project implements an **event-driven architecture** using AWS services managed with Terraform. It allows ingestion of sensor data via a REST API and stores it into an S3 bucket. CI/CD is enabled using GitHub Actions.

---

## 📁 Project Structure

```
.
├── .github/workflows/         # GitHub Actions CI/CD workflows
├── lambda/                    # Python source code for AWS Lambda
│   ├── handler.py             # Lambda function entry point
│   └── daily_report_generator.py  # (Optional) Report Lambda
├── main.tf                    # Terraform infrastructure definitions
├── outputs.tf                 # Terraform output variables
├── provider.tf                # AWS provider config
├── variables.tf               # Input variables for Terraform
├── .terraform.lock.hcl        # Terraform dependency lock file
├── .gitignore                 # Git ignore file
└── README.md                  # This file
```

---

##  Features

- REST API endpoint using API Gateway
- AWS Lambda to process JSON payload
- Store data in S3 bucket with timestamped filename
- Infrastructure-as-Code with Terraform
- CI/CD using GitHub Actions

---

## Technologies Used

- **AWS Lambda**
- **Amazon S3**
- **Amazon API Gateway (HTTP API)**
- **Terraform**
- **GitHub Actions (CI/CD)**

---

##  Terraform Workflow

### Step 1: Initialize Terraform
```bash
terraform init
```

### Step 2: Format and validate configuration
```bash
terraform fmt
terraform validate
```

### Step 3: Plan infrastructure
```bash
terraform plan
```

### Step 4: Apply infrastructure
```bash
terraform apply
```

### Step 5: Destroy when not needed
```bash
terraform destroy
```

---

## 🔄 API Usage

- **Endpoint**: `POST /sensor`
- **Content-Type**: `application/json`

Example CURL:
```bash
curl -X POST https://<api-id>.execute-api.ap-south-1.amazonaws.com/sensor \
  -H "Content-Type: application/json" \
  -d '{ "temperature": 28, "humidity": 90 }'
```

---

## 🔐 GitHub Actions Secrets Required

Go to **GitHub → Settings → Secrets** and add:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

These are used in `.github/workflows/terraform.yml` to deploy infrastructure via CI.

---

## ✅ Methodology Summary

| Stage       | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| Infrastructure | Provisioned using Terraform with remote AWS resources                    |
| API Trigger | API Gateway triggers Lambda on sensor data POST                             |
| Lambda Role | IAM role with `AWSLambdaBasicExecutionRole` and `s3:PutObject` permissions |
| Storage     | Data stored in S3 bucket with timestamp-based file name                     |
| Automation  | CI/CD pipeline using GitHub Actions on every push                           |

---

## 🧹 Cleanup

To remove all resources from AWS:

```bash
terraform destroy
```

If the S3 bucket isn’t empty, empty it manually before destruction.

---

## 👨‍💻 Author

Built by [Swaraj Pawar](https://github.com/SnakeyEye497)
