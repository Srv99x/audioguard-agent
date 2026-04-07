import argparse
import json
import os
import sys
from pathlib import Path
import subprocess

def analyze_audio(file_path):
    """Compatibility wrapper around the real acoustic analyzer script."""
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}", "file": file_path}

    project_root = Path(__file__).resolve().parents[1]
    analyzer_script = project_root / "skills" / "analyze-audio" / "scripts" / "analyze.py"
    if not analyzer_script.exists():
        return {
            "error": f"Analyzer script not found: {analyzer_script}",
            "file": file_path,
        }

    cmd = [sys.executable, str(analyzer_script), "--file", file_path]
    completed = subprocess.run(cmd, capture_output=True, text=True)

    if completed.returncode != 0:
        stderr_msg = completed.stderr.strip() or completed.stdout.strip() or "Analyzer failed"
        return {"error": stderr_msg, "file": file_path}

    try:
        payload = json.loads(completed.stdout.strip())
    except json.JSONDecodeError:
        return {
            "error": "Analyzer returned non-JSON output",
            "file": file_path,
            "raw_output": completed.stdout.strip(),
        }

    payload["wrapper_note"] = "scripts/analyze.py delegates to skills/analyze-audio/scripts/analyze.py"
    return payload

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AudioGuard analyzer compatibility wrapper")
    parser.add_argument("--file", required=True, help="Path to audio file")
    args = parser.parse_args()
    result = analyze_audio(args.file)
    print(json.dumps(result, indent=2))
