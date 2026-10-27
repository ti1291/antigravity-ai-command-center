---
name: Industrial Command Telemetry
description: High-contrast obsidian and emerald/amber engineering telemetry interface for the AI Command Center.
colors:
  primary: "#0F172A"
  secondary: "#10B981"
  tertiary: "#F59E0B"
  neutral: "#F8FAFC"
  surface: "#1E293B"
  on-surface: "#E2E8F0"
typography:
  headline-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
  body-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  label-sm:
    fontFamily: JetBrains Mono, monospace
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
rounded:
  sm: 4px
  md: 8px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
components:
  card-module:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 24px
---

# Industrial Command Telemetry

## Overview
A high-contrast, crisp engineering dashboard displaying the status of the three Antigravity external integrations: Obsidian Memory Vault, Netlify MCP Instant Hosting, and Google Cloud Run (`gcloud`).

## Colors
- **Primary (`#0F172A`):** Deep slate foundation.
- **Secondary (`#10B981`):** Emerald signal green for active connections and verified health checks.
- **Tertiary (`#F59E0B`):** Amber warning accent for action items.
- **Surface (`#1E293B`):** Elevated telemetry panel background.

## Do's and Don'ts
- Do maintain strict WCAG AA+ contrast ratios across dark slate surfaces.
- Don't use purple or violet gradients (strictly banned).
- Do use monospace typography for CLI commands and file paths.
