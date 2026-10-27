---
name: flutter-widget-generator
description: >-
  Project-scoped Flutter widget generator that scaffolds a clean-architecture Flutter widget wired to DESIGN.md tokens (AppDesignTokens) along with a matching widget test. Use when adding new Flutter UI components or screens in this repository.
---

# Flutter Widget Generator (Project Skill)

Scaffolds a production-ready Flutter widget bound to `AppDesignTokens` (`lib/theme/app_theme.dart`) plus a corresponding widget test in `test/widgets/`.

## Steps

1. **Ensure Design Tokens Are Compiled**:
   Run `custom-design-system` first if `flutter_app/lib/theme/app_theme.dart` is missing.
2. **Generate Widget + Widget Test**:
   ```powershell
   uv run python .agents/skills/flutter-widget-generator/scripts/generate_flutter_widget.py --name CommandStatusCard --project-root .
   ```
3. **Verify Files**:
   Check `flutter_app/lib/widgets/<snake_name>.dart` and `flutter_app/test/widgets/<snake_name>_test.dart`.
