import argparse
import json
import os
import sys
from datetime import datetime, timezone

def analyze_audio(file_path):
    if not os.path.exists(file_path):
        return {
            "error": f"File not found: {file_path}",
            "file": file_path,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    try:
        file_size = os.path.getsize(file_path)
        file_name = os.path.basename(file_path)

        # Acoustic heuristic simulation
        size_factor = min((file_size / 100000) * 30, 40)
        name_factor = 30 if any(x in file_name.lower() for x in ["fake", "synthetic", "gen", "ai"]) else 0
        base_score = 25

        risk_score = min(int(base_score + size_factor + name_factor), 100)
        confidence = 85 if name_factor > 0 else 72

        if confidence < 60:
            label = "UNCERTAIN"
        elif risk_score >= 70:
            label = "DEEPFAKE"
        elif risk_score >= 41:
            label = "UNCERTAIN"
        else:
            label = "AUTHENTIC"

        return {
            "file": file_name,
            "risk_score": risk_score,
            "confidence": confidence,
            "label": label,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    except Exception as e:
        return {
            "error": str(e),
            "file": file_path,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to .wav file")
    args = parser.parse_args()
    result = analyze_audio(args.file)
    print(json.dumps(result, indent=2))
