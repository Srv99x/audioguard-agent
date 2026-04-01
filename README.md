# AudioGuard Agent

An AI security agent that detects deepfake audio risks in developer pipelines.
Built for the GitAgent Hackathon 2026 using the gitagent standard.

## What It Does
- Analyzes .wav audio files for deepfake risk
- Returns risk score (0-100), confidence level, and classification
- Labels audio as AUTHENTIC, UNCERTAIN, or DEEPFAKE
- Generates structured markdown security reports

## Quick Start
```bash
npm install gitclaw
npx gitclaw run .
```

## Test the Analyzer
```bash
python scripts/analyze.py --file your-audio.wav
```

## Sample Output
```json
{
  "file": "file_example_WAV_1MG.wav",
  "risk_score": 65,
  "confidence": 72,
  "label": "UNCERTAIN",
  "timestamp": "2026-04-01T20:33:23Z"
}
```

## Agent Structure
- SOUL.md — AudioGuard identity and values
- RULES.md — Hard behavioral constraints
- skills/analyze-audio — Core detection skill
- skills/generate-report — Report generation skill
- scripts/analyze.py — Python analysis engine

## Tech Stack
- gitagent standard (spec 0.1.0)
- gitclaw runtime
- Claude Sonnet 4.6
- Python 3.14
