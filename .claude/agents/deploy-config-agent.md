---
name: deploy-config-agent
description: "[PLACEHOLDER] Infrastructure configuration agent - not yet implemented"
model: opus
color: blue
---

# Deploy Config Agent [PLACEHOLDER - NOT YET IMPLEMENTED]

This agent is a placeholder for future deployment infrastructure generation. It is part of the DCF workflow (Step 5: Deployment) but is not yet functional.

## Planned Capabilities

When implemented, this agent will:

- **Generate Infrastructure as Code (IaC)** for any completed module
- **Implement service discovery** for inter-module communication
- **Support multiple cloud providers**: AWS, Azure, GCP, and local (Docker Compose)
- **Create environment-specific configurations** (dev, staging, prod)
- **Generate deployment and validation scripts**

## Planned Provider Support

| Provider | IaC Tool | Config Store |
|----------|----------|--------------|
| AWS | CDK / CloudFormation | SSM Parameter Store |
| Azure | Bicep / ARM | Key Vault / App Configuration |
| GCP | Terraform / Deployment Manager | Secret Manager |
| Local | Docker Compose | Environment files |

## Status

This agent will be implemented in a future release. For now, deployment must be handled manually outside the DCF workflow.
