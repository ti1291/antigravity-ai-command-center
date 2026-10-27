---
name: db-seed-runner
description: >-
  Project-scoped database seeding skill for AI Command Center. Generates and loads deterministic, idempotent seed records for Firestore collections and local JSON development databases. Use when the user asks to seed the database, reset dev fixtures, or populate test collections.
---

# Database Seed Runner (Project Skill)

Populates deterministic development and staging fixtures for the AI Command Center repository (`users`, `agent_runs`, `mcp_connections`, and `deployments`).

## Steps

1. **Generate & Validate Seed Payload**:
   ```powershell
   uv run python .agents/skills/db-seed-runner/scripts/seed_database.py --output ./web-app/assets/seed-db.json
   ```
2. **Verify Idempotency**:
   Confirm that `status: "ok"` and the deterministic SHA-256 checksum match across runs.
