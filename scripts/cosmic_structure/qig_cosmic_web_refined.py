

"""
Refined QIR Cosmic Web Structure Model
Author: Christopher Patrick Booth Smolen, AXVIAM PBC
Purpose: Simulates emergence of large-scale structure under QIR's information flow field.
"""

import numpy as np
import matplotlib.pyplot as plt

def coherence_wave(x, y, f=0.02, phase=0.5, amplitude=1.0):
    """
    Generates a QIR-inspired harmonic coherence wave across a 2D grid.

    Parameters:
    - x, y: meshgrid arrays
    - f: spatial frequency
    - phase: global coherence phase offset
    - amplitude: intensity of structural memory influence

    Returns:
    - 2D field of coherence
    """
    return amplitude * np.sin(f * x + phase) * np.cos(f * y - phase)

def generate_cosmic_web(grid_size=300, f=0.02, phase=0.5, noise_level=0.01):
    """
    Generates a refined cosmic web structure from memory-based coherence patterns.

    Parameters:
    - grid_size: number of grid points
    - f: spatial frequency
    - phase: structural time-phase coherence
    - noise_level: amplitude of stochastic memory noise

    Returns:
    - 2D numpy array representing information field density
    """
    x = np.linspace(0, 2 * np.pi, grid_size)
    y = np.linspace(0, 2 * np.pi, grid_size)
    X, Y = np.meshgrid(x, y)

    wave = coherence_wave(X, Y, f=f, phase=phase)
    noise = noise_level * np.random.randn(grid_size, grid_size)
    web = wave + noise

    return web

def plot_cosmic_web(web, title="QIR Cosmic Web (Refined)"):
    plt.figure(figsize=(8, 6))
    plt.imshow(web, cmap="plasma", origin="lower")
    plt.colorbar(label="Memory-Driven Density")
    plt.title(title)
    plt.xlabel("X (arbitrary units)")
    plt.ylabel("Y (arbitrary units)")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    field = generate_cosmic_web()
    plot_cosmic_web(field)