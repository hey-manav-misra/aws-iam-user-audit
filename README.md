# AWS IAM User Audit

A Python tool for auditing AWS IAM users and their access keys across AWS accounts. This tool generates CSV reports containing user information, access key details, and last access timestamps for security analysis and compliance purposes.

## Features

- List all IAM users in an AWS account
- Export access key information with creation dates
- Track last access times for security monitoring
- Generate account-specific CSV reports
- Support for multiple AWS account auditing

## Files

- `get_details.py` - Main audit script that generates account-specific CSV files
- `.gitignore` - Excludes CSV files from version control

## Prerequisites

- Python 3.x
- boto3 library
- AWS credentials configured (via AWS CLI, environment variables, or IAM roles)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hey-manav-misra/aws-iam-user-audit.git
cd aws-iam-user-audit
```

2. Install dependencies:
```bash
pip install boto3
```

3. Configure AWS credentials:
```bash
aws configure
```

## Usage

### Basic Audit
Run the main audit script to generate a CSV report for the current AWS account:

```bash
python get_details.py
```

This creates a file named `iam_users_{account_id}.csv` with the following columns:
- Account_ID
- User_Name
- Access_Key_ID
- Created_Date
- Last_Accessed


## Output

CSV files contain sensitive information and are automatically excluded from git tracking. Reports include:

- All IAM users in the account
- Access key creation dates
- Last access timestamps for security monitoring
- Account ID for multi-account environments

## Security Notes

- CSV files containing user data are excluded from version control
- Ensure AWS credentials have appropriate IAM permissions
- Review generated reports for compliance and security analysis
- Store output files securely as they contain account information

## Required IAM Permissions

Your AWS credentials need the following permissions:
- `iam:ListUsers`
- `iam:ListAccessKeys`
- `iam:GetAccessKeyLastUsed`
- `sts:GetCallerIdentity`

## License

This project is for security auditing and compliance purposes.