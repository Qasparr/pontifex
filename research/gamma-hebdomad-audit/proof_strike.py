# 93
# ---------------------------------------------------------------------
# proof_strike.py -- the proof strike for the Beta blend curves
# seated in Resonantia (resonance/studio/blend_curves.py): a
# demonstration blend rendered from the module itself, mastered to
# the house law, and MEASURED BACK -- the crossfade weights are read
# out of the rendered audio by FFT at each segment's midpoint and
# checked against the curves' closed forms.
#
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe,
# ARR, All Rights Reserved, Without Prejudice. Written XXVI day of
# November, Anno V:xii e.n. (2026 e.v.), under the Method of Science,
# Aim of Religion -- Scientific Illuminism.
#
# DESIGN OF THE STRIKE: two sustained tones in the house field,
# A = 216 Hz and B = 324 Hz (216 x 3/2, the fifth above it in the
# 432 field), in three 4-second segments separated by 0.25 s of
# silence. In each segment the mix runs A -> B across the whole
# segment under one of the plate's curves, in the plate's order:
# symmetric_blend (I = 3t^2 - 2t^3), late_snap_blend (I = t^5),
# early_lean_blend (I = 1 - (1-t)^5 (1 + 5t)). At each segment's
# midpoint (t = 0.5) the closed forms predict the B:A amplitude
# ratio exactly: symmetric 0.5:0.5 = 1.000 (+0.00 dB); late snap
# 0.03125:0.96875 = 0.0323 (-29.83 dB); early lean
# 0.890625:0.109375 = 8.143 (+18.22 dB). A Hann-windowed FFT at each
# midpoint measures the two tones' amplitudes from the render and
# the ratios are printed against the predictions -- the proof is
# that the rendered sound carries the curves' figures, not merely
# that the functions return them.
#
# MASTERING: gain staged to the house law (-14 LUFS integrated,
# true peak <= -1.0 dBTP) and encoded at exactly 320,000 bps;
# the delivered file is re-measured and its figures printed.
# Output: proof-strike/blend-curves-proof.mp3 + figures.json.
# ---------------------------------------------------------------------

import json
import math
import subprocess
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "resonance"))

from resonance.studio.blend_curves import (  # noqa: E402
    early_lean_blend, late_snap_blend, symmetric_blend)

SR = 44100
SEG = 4.0          # seconds per segment
GAP = 0.25         # seconds of silence between segments
F_A, F_B = 216.0, 324.0
CURVES = [("symmetric", symmetric_blend, lambda t: 3 * t * t - 2 * t ** 3),
          ("late_snap", late_snap_blend, lambda t: t ** 5),
          ("early_lean", early_lean_blend,
           lambda t: 1 - (1 - t) ** 5 * (1 + 5 * t))]


def render():
    """Three segments, each a full A -> B crossfade under one curve,
    mixed as (1 - w) * A + w * B with w the module's own blend()."""
    n_seg, n_gap = int(SEG * SR), int(GAP * SR)
    t_seg = np.arange(n_seg) / SR
    tone_a = np.sin(2 * np.pi * F_A * t_seg)
    tone_b = np.sin(2 * np.pi * F_B * t_seg)
    parts = []
    for i, (_, fn, _) in enumerate(CURVES):
        w = np.array([fn(t / SEG) for t in t_seg])
        parts.append((1 - w) * tone_a + w * tone_b)
        if i < len(CURVES) - 1:
            parts.append(np.zeros(n_gap))
    mono = np.concatenate(parts) * 0.5
    return np.stack([mono, mono], axis=1)  # stereo, identical sides


def measure_ratios(audio):
    """Hann-windowed FFT at each segment midpoint: the measured
    B:A amplitude ratio beside the closed form's prediction."""
    mono = audio[:, 0]
    rows = []
    win_n = SR // 2
    for i, (name, _, closed) in enumerate(CURVES):
        mid = int((i * (SEG + GAP) + SEG / 2) * SR)
        seg = mono[mid - win_n // 2: mid + win_n // 2]
        spec = np.abs(np.fft.rfft(seg * np.hanning(len(seg))))
        freqs = np.fft.rfftfreq(len(seg), 1 / SR)
        a_amp = spec[np.argmin(np.abs(freqs - F_A))]
        b_amp = spec[np.argmin(np.abs(freqs - F_B))]
        measured = b_amp / a_amp
        w = closed(0.5)
        predicted = w / (1 - w)
        rows.append({
            "segment": name,
            "weight_at_midpoint": w,
            "predicted_ratio": predicted,
            "predicted_db": 20 * math.log10(predicted),
            "measured_ratio": float(measured),
            "measured_db": float(20 * math.log10(measured)),
            "error_db": float(abs(20 * math.log10(measured / predicted))),
        })
    return rows


def loudnorm_measure(path):
    out = subprocess.run(
        ["ffmpeg", "-i", str(path), "-af",
         "loudnorm=print_format=json", "-f", "null", "-"],
        capture_output=True, text=True).stderr
    block = out[out.rindex("{"):out.rindex("}") + 1]
    return json.loads(block)


def main():
    out_dir = HERE / "proof-strike"
    out_dir.mkdir(exist_ok=True)
    audio = render()
    ratios = measure_ratios(audio)

    wav = out_dir / "blend-raw.wav"
    pcm = (audio * 32767).astype("<i2")
    import wave
    with wave.open(str(wav), "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(SR)
        wf.writeframes(pcm.tobytes())

    first = loudnorm_measure(wav)
    gain = -14.0 - float(first["input_i"])
    mp3 = out_dir / "blend-curves-proof.mp3"
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(wav), "-af", f"volume={gain:.3f}dB",
         "-codec:a", "libmp3lame", "-b:a", "320k", str(mp3)],
        capture_output=True, check=True)
    final = loudnorm_measure(mp3)
    probe = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=bit_rate",
         "-of", "json", str(mp3)], capture_output=True, text=True)
    figures = {
        "file": mp3.name,
        "gain_applied_db": round(gain, 3),
        "integrated_lufs": float(final["input_i"]),
        "true_peak_dbtp": float(final["input_tp"]),
        "bit_rate": int(json.loads(probe.stdout)["format"]["bit_rate"]),
        "ratios": ratios,
    }
    (out_dir / "figures.json").write_text(json.dumps(figures, indent=2))
    print(json.dumps(figures, indent=2))
    wav.unlink()


if __name__ == "__main__":
    main()
