# Memory

This file stores persistent operational knowledge for AudioGuard across runs.

## Detection Notes

- Use this section to record repeated feature patterns seen in confirmed deepfakes.
- Include only validated patterns (avoid one-off assumptions).

## False Positive Cases

- Track audio files that were flagged but later verified authentic.
- Include likely causes (noise floor, compression artifacts, clipping, etc.).

## False Negative Cases

- Track files missed by the model and how they were later confirmed synthetic.
- Note which features looked normal despite synthetic origin.

## Environment Notes

- Preferred analyzer: skills/analyze-audio/scripts/analyze.py
- If librosa is missing, fallback analyzer confidence is lower by design.

## Update Format

- Timestamp (UTC):
- File:
- Verdict:
- Confidence:
- Key signals:
- Follow-up action:
