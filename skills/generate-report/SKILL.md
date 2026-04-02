---
name: generate-report
description: "Generates a markdown security audit report from audio analysis results"
allowed-tools: Read Write cli
---

# Generate Report

## Purpose
Format analyze-audio output into a structured markdown security report.

## Steps
1. Accept JSON output from analyze-audio skill (passed as a string)
2. Run: python skills/generate-report/scripts/report.py --analysis '<json_string>' --output-dir reports
3. Parse the JSON output from report.py to get the report path and classification
4. Read the generated report file and display its contents to the user
5. Inform the user where the report was saved
