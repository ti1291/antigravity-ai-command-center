#!/usr/bin/env python3
"""Deterministic Database Seeding Utility for AI Command Center."""

from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

SEED_COLLECTIONS = {
    "mcp_connections": [
        {"id": "mcp-netlify", "name": "Netlify Direct Hosting", "transport": "stdio", "status": "connected"},
        {"id": "mcp-obsidian", "name": "Obsidian Vault Memory", "transport": "stdio", "status": "connected"},
        {"id": "mcp-assets", "name": "Contextual Assets (NotebookLM)", "transport": "stdio", "status": "connected"},
    ],
    "skills_registry": [
        {"id": "skill-json-cleaner", "scope": "global", "path": "~/.gemini/config/skills/json-data-cleaner"},
        {"id": "skill-design-system", "scope": "global", "path": "~/.gemini/config/skills/custom-design-system"},
        {"id": "skill-netlify-preview", "scope": "global", "path": "~/.gemini/config/skills/netlify-preview-pipeline"},
        {"id": "skill-notebooklm-assets", "scope": "global", "path": "~/.gemini/config/skills/notebooklm-asset-extractor"},
        {"id": "skill-db-seed", "scope": "project", "path": ".agents/skills/db-seed-runner"},
        {"id": "skill-flutter-widget", "scope": "project", "path": ".agents/skills/flutter-widget-generator"},
        {"id": "skill-firebase-sync", "scope": "project", "path": ".agents/skills/firebase-sync-workflow"},
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Seed deterministic project database fixtures.")
    parser.add_argument("--output", type=Path, required=True, help="Target seed JSON file path")
    args = parser.parse_args()

    payload_bytes = json.dumps(SEED_COLLECTIONS, sort_keys=True).encode("utf-8")
    checksum = hashlib.sha256(payload_bytes).hexdigest()[:16]

    document = {
        "schemaVersion": "1.0.0",
        "checksum": checksum,
        "collections": SEED_COLLECTIONS,
    }

    out_path = args.output.resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "status": "ok",
                "output": str(out_path),
                "checksum": checksum,
                "collections_seeded": len(SEED_COLLECTIONS),
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
