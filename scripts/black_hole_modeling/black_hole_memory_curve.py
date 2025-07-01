"""
QIR Black Hole Memory Curve Simulation
Author: Christopher Patrick Booth Smolen, AXVIAM PBC
Purpose: Simulate memory field variation inside and around black hole horizons under QIR.
"""

import numpy as np
import matplotlib.pyplot as plt

def memory_profile(r, rs, I0=1.0, decay_scale=1.5):
    """
    Defines the QIR memory intensity profile around a black hole.

    Parameters:
    - r: array of radial distances (in units of Schwarzschild radius)
    - rs: Schwarzschild radius (can normalize r/rs externally)
    - I0: initial memory intensity
    - decay_scale: scale of information diffusion across event horizon

    Returns:
    - I(r): memory intensity field across radial domain
    """
    r_ratio = r / rs
    I_r = I0 * np.exp(-decay_scale * (r_ratio - 1)**2)
    return I_r

def plot_memory_profile(rs=1.0, I0=1.0, decay_scale=1.5):
    r = np.linspace(0.5 * rs, 3 * rs, 1000)
    I_r = memory_profile(r, rs, I0, decay_scale)

    plt.figure(figsize=(8, 5))
    plt.plot(r / rs, I_r, label="QIR Memory Intensity")
    plt.axvline(1.0, color='red', linestyle='--', label="Event Horizon (r = r_s)")
    plt.xlabel("Radial Distance (r / r_s)")
    plt.ylabel("Memory Field Intensity I(r)")
    plt.title("QIR Black Hole Memory Curve")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_memory_profile()
