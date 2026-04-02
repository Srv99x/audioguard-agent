---
name: analyze-audio
description: "Analyzes a .wav audio file for deepfake risk using acoustic feature extraction"
allowed-tools: Read Write cli
---

# Analyze Audio

## Purpose
Detect whether a given audio file is synthetic (deepfake) or authentic using real acoustic feature extraction.

## Steps
1. Accept a file path to a .wav audio file
2. Validate the file exists and is readable - if not, log the error and stop
3. Run: python skills/analyze-audio/scripts/analyze.py --file <path>
4. Parse the JSON output which contains: score, confidence, features
5. Classify using these rules:
   - If confidence < 60%: override label to UNCERTAIN regardless of score
   - Score 0-40: AUTHENTIC
   - Score 41-69: UNCERTAIN
   - Score 70-100: DEEPFAKE
6. Pass the full JSON result string to the generate-report skill
