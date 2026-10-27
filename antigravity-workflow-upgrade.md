# Antigravity Workflow Upgrade Plan

## Goal
Implement the 3-pillar Antigravity power-user architecture across global configuration (`~/.gemini/config/`) and the starter workspace (`C:/Users/vanes/.gemini/antigravity/scratch/ai-command-center/`):
1. **The `AGENTS.md` Framework** (Sequential Plan, Request Clarity, Background Async Task Declaration before file edits)
2. **MCP Server Pipelines** (Netlify Direct Hosting Pipeline + Contextual Asset / NotebookLM MCP bridge)
3. **Global (`~/.gemini/config/skills/`) & Project-Scoped (`.agents/skills/`) Modular Skills**

## Project Type
**FULL-STACK (WEB + FLUTTER + FIREBASE + NETLIFY)**

## Tasks
- [x] **Task 1: Global `AGENTS.md` Prompt Formula** (`C:/Users/vanes/.gemini/config/rules/AGENTS.md`) → Enforce sequential plan outline, clarity gate, and async background task declaration before file rewrites. → **Verify:** File exists and is under 24KB rule cap.
- [x] **Task 2: Project Root `AGENTS.md` Upgrade** (`C:/Users/vanes/.gemini/antigravity/scratch/ai-command-center/AGENTS.md` & `scratch/AGENTS.md`) → Add the structured Prompt Formula template, MCP pipeline bindings, and skill routing table. → **Verify:** Inspect `AGENTS.md` sections.
- [x] **Task 3: MCP Server Integration (`mcp_config.json` + `contextual-assets/`)** → Configure `netlify`, `obsidian-vault`, and `contextual-assets` MCP servers in `C:/Users/vanes/.gemini/config/mcp_config.json` and initialize `contextual-assets/`. → **Verify:** Validate JSON syntax with Python `json.load`.
- [x] **Task 4: Global Skill 1 — `json-data-cleaner`** (`C:/Users/vanes/.gemini/config/skills/json-data-cleaner/`) → Create `SKILL.md` and `scripts/clean_json_data.py` for cross-workspace JSON/CSV/JSONL formatting, deduplication, and schema validation. → **Verify:** Run `uv run python clean_json_data.py --self-test`.
- [x] **Task 5: Global Skill 2 — `custom-design-system`** (`C:/Users/vanes/.gemini/config/skills/custom-design-system/`) → Create `SKILL.md` and `scripts/sync_design_tokens.py` to compile `DESIGN.md` tokens into CSS variables and Flutter `ThemeData`. → **Verify:** Run script against `ai-command-center/DESIGN.md`.
- [x] **Task 6: Global Skill 3 & 4 — `netlify-preview-pipeline` & `notebooklm-asset-extractor`** (`C:/Users/vanes/.gemini/config/skills/`) → Create global skills for automated Netlify preview deploys and NotebookLM/contextual asset ingestion. → **Verify:** Run `extract_contextual_assets.py` on `contextual-assets/`.
- [x] **Task 7: Project-Scoped Skills (`.agents/skills/`)** (`db-seed-runner`, `flutter-widget-generator`, `firebase-sync-workflow`) → Create workspace-specific skills and helper scripts in `ai-command-center/.agents/skills/`. → **Verify:** Execute all 3 project skill scripts in dry-run/test mode.

## Phase X: Verification
- [x] All `SKILL.md` frontmatters have valid `name` and `description` fields.
- [x] `mcp_config.json` parses cleanly (`MCP_JSON_OK`).
- [x] Helper scripts execute with exit code 0.

## ✅ PHASE X COMPLETE
- Lint & JSON Schema: ✅ Pass
- Security (Token & Secret Scan): ✅ No critical issues
- Build & Asset Extraction: ✅ Success
- Date: 2026-10-27
