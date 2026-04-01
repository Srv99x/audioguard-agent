---
name: analyze-audio
description: "Analyzes a .wav audio file for deepfake risk using acoustic feature extraction"
allowed-tools: Bash Read Write
---

# Analyze Audio

## Purpose
Detect whether a given audio file is synthetic or authentic.

## Steps
1. Accept a file path to a .wav audio file
2. Validate the file exists and is readable - if not, log the error and stop
3. Run: python scripts/analyze.py --file <path>
4. Parse the JSON output
5. Classify:
   - Score 0-40: AUTHENTIC
   - Score 41-69: UNCERTAIN
   - Score 70-100: DEEPFAKE
6. If confidence below 60%, override label to UNCERTAIN
7. Pass result to generate-report skill
