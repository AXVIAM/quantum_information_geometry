

"""
Gravitational Wave Feedback via QIR Memory Field
Author: Christopher Patrick Booth Smolen, AXVIAM PBC
Purpose: Simulate echo patterns and waveform deviations from QIR memory feedback in post-merger black holes.
"""

import numpy as np
import matplotlib.pyplot as plt

def waveform_with_memory(t, A=1.0, f=150, decay=0.01, I_strength=0.02, phase_delay=0.005):
    """
    Generate a simple ringdown waveform modified by QIR memory feedback.

    Parameters:
    - t: time array (seconds)
    - A: base amplitude
    - f: base frequency (Hz)
    - decay: exponential decay rate
    - I_strength: strength of feedback oscillation due to memory field
    - phase_delay: time delay for echo feedback

    Returns:
    - waveform: array of gravitational wave strain with QIR feedback
    """
    base = A * np.exp(-decay * t) * np.sin(2 * np.pi * f * t)
    echo = I_strength * np.exp(-decay * (t - phase_delay)) * np.sin(2 * np.pi * f * (t - phase_delay))
    echo[t < phase_delay] = 0  # Zero out pre-delay region
    return base + echo

def plot_waveform():
    t = np.linspace(0, 0.1, 2000)
    h = waveform_with_memory(t)

    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, h, label="QIR-Modified Ringdown", linewidth=1.5)
    plt.xlabel("Time (ms)")
    plt.ylabel("Strain (a.u.)")
    plt.title("Gravitational Waveform with QIR Memory Feedback")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_waveform()