# AWS S3 Terraform Practice

## Overview
This project demonstrates using Terraform to provision and manage an Amazon S3 bucket.

## Tools
- Terraform
- AWS
- Amazon S3
- Git and GitHub

## What I Practiced
- Configuring the AWS Terraform provider in `us-east-1`
- Initializing and validating a Terraform configuration
- Reviewing changes with `terraform plan`
- Creating an S3 bucket with `terraform apply`
- Verifying the resource with AWS CLI and Terraform state
- Removing the resource with `terraform destroy`
- Confirming the final plan showed no changes

## Cleanup
The practice S3 bucket was destroyed after verification. The configuration was then updated so Terraform would not propose recreating the bucket.

## Safety
Terraform state files and the `.terraform` provider directory are excluded from Git using `.gitignore`.
