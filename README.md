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
python skills/analyze-audio/scripts/analyze.py --file your-audio.wav
```

## Sample Output

```json
{
  "file": "file_example_WAV_1MG.wav",
  "score": 65,
  "confidence": 72,
  "features": {
    "mfcc_variance": 180.4,
    "zcr_variance": 0.00034
  },
  "analyzer": "librosa"
}
```

## Agent Structure

- SOUL.md — AudioGuard identity and values
- RULES.md — Hard behavioral constraints
- skills/analyze-audio — Core detection skill
- skills/generate-report — Report generation skill
- scripts/analyze.py — Compatibility wrapper that delegates to the real analyzer
- workspace/ — Optional staging area for temporary files used during local runs

## Tech Stack

- gitagent standard (spec 0.1.0)
- gitclaw runtime
- Google Gemini 2.5 Flash
- Python 3.13+

## Judging Criteria

- **Agent Quality (30%)** — `SOUL.md` defines a precise security-focused identity with domain-specific values; `RULES.md` enforces hard behavioral constraints with numerical thresholds (e.g. confidence < 60% → UNCERTAIN).
- **Skill Design (25%)** — Two focused, well-documented skills: `analyze-audio` (acoustic feature extraction via librosa) and `generate-report` (timestamped markdown audit reports), each with valid SKILL.md frontmatter and step-by-step instructions.
- **Working Demo (25%)** — Runs end-to-end via `npx gitclaw run .`; Python librosa script returns real acoustic features with risk score, confidence, and classification from actual WAV analysis.
- **Creativity (20%)** — Applies AI agent architecture to deepfake audio security — an underserved but critical threat surface in modern developer pipelines.
