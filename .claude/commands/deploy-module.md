---
description: "[PLACEHOLDER] Generate deployment config and deploy module - not yet implemented"
model: claude-opus-4-5-20251101
---

# /deploy-module [PLACEHOLDER - NOT YET IMPLEMENTED]

This command is a placeholder for future module deployment. It is part of the DCF workflow (Step 5: Deployment) but is not yet functional.

## Planned Switches

- `-module` -> Module ID to deploy (e.g., M1, M2). Required.
- `-provider` -> Target cloud provider: aws, azure, gcp, local (default: local)
- `-environment` -> Target environment: dev, staging, prod (default: dev)
- `-dry-run` -> Generate config only, don't execute deployment

## Planned Behavior

When implemented, this command will:

1. **Validate module readiness** — verify L1/L2 test gates passed and dependencies deployed
2. **Invoke deploy-config-agent** — generate IaC configurations for the target provider
3. **Execute deployment** — run provider-specific deployment scripts (unless `--dry-run`)
4. **Update tracking** — mark module as `Deployed` in `tracking/module-tracking.md`

## Supported Providers (Planned)

- **aws** — AWS CDK / CloudFormation
- **azure** — Azure Bicep / ARM templates
- **gcp** — Terraform / Deployment Manager
- **local** — Docker Compose

## Status

This command will be implemented in a future release. For now, deployment must be handled manually outside the DCF workflow.

## Related

- `/generate-code`: Implement and test modules (prerequisite for deployment)
- `deploy-config-agent`: Infrastructure configuration agent (also placeholder)
