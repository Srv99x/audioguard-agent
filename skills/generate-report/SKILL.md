---
name: generate-report
description: "Generates a markdown security audit report from audio analysis results"
allowed-tools: Read Write
---

# Generate Report

## Purpose
Format analyze-audio output into a structured markdown security report.

## Steps
1. Accept JSON output from analyze-audio skill
2. Create reports/ directory if it does not exist
3. Generate report_<filename>.md with:
   - File analyzed
   - Risk score and confidence
   - Classification label
   - Timestamp
   - Recommended action:
     AUTHENTIC: No action needed
     UNCERTAIN: Manual review recommended
     DEEPFAKE: Block immediately, escalate to security team
4. Save to reports/report_<filename>.md
