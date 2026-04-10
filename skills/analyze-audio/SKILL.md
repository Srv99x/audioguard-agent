---
name: analyze-audio
description: Analyzes a .wav audio file for deepfake risk using acoustic feature extraction
allowed-tools: Read Write cli
confidence: 1
usage_count: 1
success_count: 1
failure_count: 0
negative_examples: []
---

# Analyze Audio

## Purpose
Detect whether a given audio file is synthetic (deepfake) or authentic using real acoustic feature extraction.

## Steps
1. Accept a file path to an audio file (prefer `.wav`; process other formats when loadable)
2. Validate the file exists and is readable - if not, log the error and stop
3. Resolve the analyzer script path relative to project root, then run: python skills/analyze-audio/scripts/analyze.py --file <path>
4. Parse the JSON output which contains: score, confidence, features
5. Classify using these rules:
   - If confidence < 60%: override label to UNCERTAIN regardless of score
   - Score 0-40: AUTHENTIC
   - Score 41-69: UNCERTAIN
   - Score 70-100: DEEPFAKE
6. Pass the full JSON result string to the generate-report skill
