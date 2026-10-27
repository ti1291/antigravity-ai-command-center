---
name: firebase-sync-workflow
description: >-
  Project-scoped Firebase configuration and security validation workflow. Checks firebase.json, firestore.indexes.json, and ensures firestore.rules does not contain open wildcard allow rules before syncing with Firebase. Remind the agent to delegate authoring firestore.rules to the firestore-rules-author subagent.
---

# Firebase Sync Workflow (Project Skill)

Validates local Firebase project configuration (`firebase.json`, `firestore.indexes.json`) and performs a static safety gate on `firestore.rules` before running `firebase deploy --only firestore`.

> **Important**: Whenever creating or modifying `firestore.rules`, always delegate the rules authoring itself to the `firestore-rules-author` subagent.

## Steps

1. **Run Pre-Sync Validation (`-CheckOnly`)**:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .agents/skills/firebase-sync-workflow/scripts/sync_firebase.ps1 -ProjectRoot . -CheckOnly
   ```
2. **Sync Indexes & Config (After Approval)**:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .agents/skills/firebase-sync-workflow/scripts/sync_firebase.ps1 -ProjectRoot .
   ```
