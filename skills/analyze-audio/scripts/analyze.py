import argparse
import json
import os
import sys
import wave
import struct
import math

def analyze(filepath):
    """
    Analyzes a WAV audio file for deepfake risk using acoustic feature extraction.
    Uses only Python standard library + numpy/scipy if available, falls back to pure Python.
    """
    if not os.path.exists(filepath):
        print(json.dumps({"error": f"File not found: {filepath}"}))
        sys.exit(1)

    try:
        # Try with librosa (full analysis)
        import numpy as np
        import librosa

        y, sr = librosa.load(filepath, sr=None, mono=True)
        duration = librosa.get_duration(y=y, sr=sr)

        # --- Feature 1: Spectral Centroid (unnatural if very flat or peaky) ---
        spectral_centroid = float(np.mean(librosa.feature.spectral_centroid(y=y, sr=sr)))
        spectral_centroid_var = float(np.var(librosa.feature.spectral_centroid(y=y, sr=sr)))

        # --- Feature 2: Zero Crossing Rate (synthetic audio is often uniformly smooth) ---
        zcr = float(np.mean(librosa.feature.zero_crossing_rate(y)))
        zcr_var = float(np.var(librosa.feature.zero_crossing_rate(y)))

        # --- Feature 3: MFCC variance (deepfakes tend to have low MFCC variance) ---
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfcc_variance = float(np.mean(np.var(mfccs, axis=1)))

        # --- Feature 4: Spectral Rolloff (checks frequency distribution naturalness) ---
        rolloff = float(np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr)))
        rolloff_var = float(np.var(librosa.feature.spectral_rolloff(y=y, sr=sr)))

        # --- Feature 5: RMS Energy (very flat energy = likely synthetic) ---
        rms = librosa.feature.rms(y=y)
        rms_mean = float(np.mean(rms))
        rms_var = float(np.var(rms))

        # --- Scoring heuristics ---
        # Natural human speech: high MFCC variance, moderate ZCR, non-flat spectral centroid
        score = 0
        confidence = 75

        # Low MFCC variance = synthetic indicator (+30 points)
        if mfcc_variance < 100:
            score += 30
        elif mfcc_variance < 300:
            score += 15

        # Very uniform ZCR = synthetic (+20 points)
        if zcr_var < 0.0001:
            score += 20
        elif zcr_var < 0.001:
            score += 10

        # Flat RMS energy = synthetic (+25 points)
        if rms_var < 0.0001:
            score += 25
            confidence += 10
        elif rms_var < 0.001:
            score += 12

        # Extreme spectral centroid (very high or very low) = synthetic (+15 points)
        if spectral_centroid < 500 or spectral_centroid > 8000:
            score += 15
        elif spectral_centroid_var < 10000:
            score += 10

        # Very low rolloff variance = synthetic (+10 points)
        if rolloff_var < 100000:
            score += 10

        # Clamp score to 0-100
        score = min(100, max(0, score))
        confidence = min(98, max(50, confidence))

        result = {
            "file": filepath,
            "duration_seconds": round(duration, 2),
            "sample_rate": sr,
            "score": score,
            "confidence": int(confidence),
            "features": {
                "spectral_centroid": round(spectral_centroid, 2),
                "spectral_centroid_variance": round(spectral_centroid_var, 2),
                "zero_crossing_rate": round(zcr, 6),
                "zcr_variance": round(zcr_var, 8),
                "mfcc_variance": round(mfcc_variance, 2),
                "rms_energy_mean": round(rms_mean, 6),
                "rms_energy_variance": round(rms_var, 8),
                "spectral_rolloff": round(rolloff, 2),
                "spectral_rolloff_variance": round(rolloff_var, 2),
            },
            "analyzer": "librosa"
        }

    except ImportError:
        # Fallback: pure Python wave analysis
        result = _analyze_pure_python(filepath)

    print(json.dumps(result))


def _analyze_pure_python(filepath):
    """Fallback analyzer using only Python's standard wave module."""
    try:
        with wave.open(filepath, 'rb') as wf:
            channels = wf.getnchannels()
            sample_width = wf.getsampwidth()
            framerate = wf.getframerate()
            n_frames = wf.getnframes()
            duration = n_frames / framerate

            raw = wf.readframes(n_frames)
            fmt = f"<{n_frames * channels}h" if sample_width == 2 else f"<{n_frames * channels}B"
            samples = struct.unpack(fmt, raw[:n_frames * channels * sample_width])

            # Basic stats
            mean = sum(samples) / len(samples)
            variance = sum((s - mean) ** 2 for s in samples) / len(samples)
            std = math.sqrt(variance)

            # Zero crossing rate
            crossings = sum(1 for i in range(1, len(samples)) if (samples[i] >= 0) != (samples[i-1] >= 0))
            zcr = crossings / len(samples)

            # Heuristic scoring (less accurate without FFT)
            score = 20 if std < 1000 else 0
            score += 15 if zcr < 0.01 else 0

            return {
                "file": filepath,
                "duration_seconds": round(duration, 2),
                "sample_rate": framerate,
                "score": score,
                "confidence": 50,
                "features": {
                    "amplitude_mean": round(mean, 2),
                    "amplitude_variance": round(variance, 2),
                    "amplitude_std": round(std, 2),
                    "zero_crossing_rate": round(zcr, 6),
                },
                "analyzer": "pure-python-fallback",
                "note": "Install librosa for full acoustic analysis: pip install librosa"
            }
    except Exception as e:
        return {"error": str(e), "file": filepath}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AudioGuard deepfake audio analyzer")
    parser.add_argument("--file", required=True, help="Path to the WAV audio file to analyze")
    args = parser.parse_args()
    analyze(args.file)
