# Workspace Rules — AI Command Center (`AGENTS.md` Framework)

> Always-active project root prompt formula connecting Antigravity to the Sequential Execution Protocol, Local Obsidian Vault, Netlify Direct Hosting MCP, Contextual Asset Links (NotebookLM), and Global/Project Skills.

---

## 1. The `AGENTS.md` Explicit Prompt Formula (Pre-Rewrite Protocol)

Before modifying or rewriting repository files, you MUST follow this 3-step sequence:

1. **Outline the Plan (`PLAN`)**:
   - List the exact files to be created or modified in sequential order (`INPUT → ACTION → VERIFY`).
   - Check `.agents/memory/MEMORY.md` and `DESIGN.md` before touching code or UI.
2. **Request Clarity (`CLARIFY`)**:
   - If scope, environment targets, or security boundaries are ambiguous, stop and ask before rewriting files.
3. **State Background Async Tasks Sequentially (`ASYNC DECLARATION`)**:
   - Explicitly declare any background commands (`IsDaemon` / async `run_command`), subagent delegations (`invoke_subagent`), or scheduled jobs before launching them.
   - Execute file writes sequentially—never mutate files while a background build, test runner, or subagent is writing to the same paths.

---

## 2. Outside Party MCP Server Pipelines 🔌

### A. Direct Hosting Pipeline (`netlify` MCP)
- Configured in `C:/Users/vanes/.gemini/config/mcp_config.json`.
- Once local debugging and build verification pass, compile and publish to a live preview URL using the `netlify` MCP tools or the global skill script:
  `powershell -ExecutionPolicy Bypass -File C:/Users/vanes/.gemini/config/skills/netlify-preview-pipeline/scripts/publish_preview.ps1 -ProjectDir ./web-app`
- Never hardcode `NETLIFY_PERSONAL_ACCESS_TOKEN` or `NETLIFY_AUTH_TOKEN` in repository files.

### B. Contextual Asset Links (`contextual-assets` & `obsidian-vault` MCP)
- **NotebookLM & Media Assets**: Drop audio logs (`.mp3`, `.wav`, `.m4a`), raw data infographic specs (`.json`, `.csv`), or video scripts (`.md`) into `contextual-assets/`.
- Run `python C:/Users/vanes/.gemini/config/skills/notebooklm-asset-extractor/scripts/extract_contextual_assets.py --source ./contextual-assets --target ./web-app/assets` to index and wire assets directly into the application codebase.
- **Obsidian Session Memory**:
  - Read `obsidian-vault/01-Team-Data.md`, `02-Project-Roadmap.md`, and `03-Built-Features-Log.md` at session start.
  - After shipping features or deployments, run `powershell -ExecutionPolicy Bypass -File .agents/skills/obsidian-memory-sync/scripts/sync-obsidian-memory.ps1`.

### C. Google Cloud Platform (`gcloud`) Protocol
- Always follow `.agents/skills/gcp-cloud-run-deploy/SKILL.md` and prepend `gcloud` commands with `$env:CLOUDSDK_METRICS_ENVIRONMENT = "datacloud.antigravity"`.

### D. GitHub Repository & PR Pipeline (`github` MCP)
- Configured in `C:/Users/vanes/.gemini/config/mcp_config.json` via `@modelcontextprotocol/server-github`.
- Verify token readiness with `powershell -ExecutionPolicy Bypass -File C:/Users/vanes/.gemini/config/skills/github-mcp-workflow/scripts/verify_github_mcp.ps1 -CheckOnly`.
- Never hardcode `GITHUB_PERSONAL_ACCESS_TOKEN` in repository files.

---

## 3. Global & Project-Scoped Skills Index 🛠️

| Scope | Skill Name | Path | Trigger / Purpose |
| :--- | :--- | :--- | :--- |
| **Global** | `json-data-cleaner` | `~/.gemini/config/skills/json-data-cleaner/` | Clean, format, deduplicate, and schema-validate JSON, JSONL, and CSV files. |
| **Global** | `custom-design-system` | `~/.gemini/config/skills/custom-design-system/` | Compile `DESIGN.md` tokens into CSS (`tokens.css`) and Flutter (`app_theme.dart`). |
| **Global** | `netlify-preview-pipeline` | `~/.gemini/config/skills/netlify-preview-pipeline/` | Build, verify, and publish live preview sites via Netlify MCP/CLI. |
| **Global** | `notebooklm-asset-extractor` | `~/.gemini/config/skills/notebooklm-asset-extractor/` | Extract NotebookLM audio logs, data infographics, and video scripts into codebase assets. |
| **Project** | `db-seed-runner` | `.agents/skills/db-seed-runner/` | Deterministically seed local/Firestore/SQL database fixtures for this repository. |
| **Project** | `flutter-widget-generator` | `.agents/skills/flutter-widget-generator/` | Scaffold a clean-architecture Flutter widget + `@Preview` + widget test using `DESIGN.md`. |
| **Project** | `firebase-sync-workflow` | `.agents/skills/firebase-sync-workflow/` | Validate `firestore.rules`, indexes, and `firebase.json` before syncing with Firebase. |
| **Project** | `netlify-deploy` | `.agents/skills/netlify-deploy/` | Workspace-specific Netlify production/preview deployment script. |
| **Project** | `gcp-cloud-run-deploy` | `.agents/skills/gcp-cloud-run-deploy/` | Workspace-specific Cloud Run source deploy (`us-central1`). |
| **Project** | `obsidian-memory-sync` | `.agents/skills/obsidian-memory-sync/` | Synchronize `obsidian-vault/` notes with `.agents/memory/MEMORY.md`. |
