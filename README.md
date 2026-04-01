# AudioGuard Agent

An AI agent that detects deepfake audio risks in developer pipelines.
Built for the GitAgent Hackathon 2026.

## Install
```
npm install gitclaw
```

## Run
```
npx gitclaw run .
```

## Analyze a file
```
python scripts/analyze.py --file your-audio.wav
```

## Sample Output
```json
{
  "file": "sample.wav",
  "risk_score": 82,
  "confidence": 91,
  "label": "DEEPFAKE",
  "timestamp": "2026-04-03T10:22:00Z"
}
```

## Tech Stack
- gitagent standard
- gitclaw runtime
- Claude Sonnet 4.6
- Python 3
