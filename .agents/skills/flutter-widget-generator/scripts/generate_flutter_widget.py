#!/usr/bin/env python3
"""Scaffold a token-bound Flutter Widget and WidgetTest for the project."""

from __future__ import annotations
import argparse
import json
import re
from pathlib import Path


def to_snake_case(name: str) -> str:
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def build_widget_code(class_name: str) -> str:
    return f"""import 'package:flutter/material.dart';
import '../theme/app_theme.dart';

class {class_name} extends StatelessWidget {{
  final String title;
  final String subtitle;

  const {class_name}({{
    super.key,
    required this.title,
    required this.subtitle,
  }});

  @override
  Widget build(BuildContext context) {{
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: AppDesignTokens.bgSurface,
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: AppDesignTokens.borderSubtle),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisSize: MainAxisSize.min,
        children: [
          Text(
            title,
            style: const TextStyle(
              color: AppDesignTokens.textPrimary,
              fontSize: 16,
              fontWeight: FontWeight.w600,
            ),
          ),
          const SizedBox(height: 6),
          Text(
            subtitle,
            style: const TextStyle(
              color: AppDesignTokens.textSecondary,
              fontSize: 13,
            ),
          ),
        ],
      ),
    );
  }}
}}
"""


def build_widget_test(class_name: str, snake_name: str) -> str:
    return f"""import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import '../../lib/widgets/{snake_name}.dart';

void main() {{
  testWidgets('{class_name} renders title and subtitle', (WidgetTester tester) async {{
    await tester.pumpWidget(
      const MaterialApp(
        home: Scaffold(
          body: {class_name}(
            title: 'MCP Server Online',
            subtitle: 'Netlify Direct Hosting Pipeline active',
          ),
        ),
      ),
    );

    expect(find.text('MCP Server Online'), findsOneWidget);
    expect(find.text('Netlify Direct Hosting Pipeline active'), findsOneWidget);
  }});
}}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Flutter widget + widget test.")
    parser.add_argument("--name", type=str, required=True, help="PascalCase widget class name")
    parser.add_argument("--project-root", type=Path, required=True, help="Project root path")
    args = parser.parse_args()

    snake = to_snake_case(args.name)
    root = args.project_root.resolve()
    widget_path = root / "flutter_app" / "lib" / "widgets" / f"{snake}.dart"
    test_path = root / "flutter_app" / "test" / "widgets" / f"{snake}_test.dart"

    widget_path.parent.mkdir(parents=True, exist_ok=True)
    test_path.parent.mkdir(parents=True, exist_ok=True)

    widget_path.write_text(build_widget_code(args.name), encoding="utf-8")
    test_path.write_text(build_widget_test(args.name, snake), encoding="utf-8")

    print(
        json.dumps(
            {
                "status": "ok",
                "widget": str(widget_path),
                "test": str(test_path),
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
