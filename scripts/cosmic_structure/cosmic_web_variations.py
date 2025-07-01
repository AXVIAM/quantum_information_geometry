"""
Cosmic Web Variations - QIR Model
Author: Christopher Patrick Booth Smolen, AXVIAM PBC
Purpose: Simulate large-scale structure formation under information-based gravitational potential.
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_density_field(grid_size=100, scale=50, coherence_amplitude=0.005):
    """
    Generates a 2D scalar density field representing initial large-scale structure influenced by QIR.

    Parameters:
    - grid_size: number of grid points along each axis
    - scale: wavelength scale of structure (larger = smoother)
    - coherence_amplitude: amplitude of information-coherence variation

    Returns:
    - 2D numpy array of density field values
    """
    x = np.linspace(0, 2 * np.pi, grid_size)
    y = np.linspace(0, 2 * np.pi, grid_size)
    X, Y = np.meshgrid(x, y)

    # Simple harmonic field perturbed by random noise to simulate structural memory pattern
    field = (
        np.sin(X * scale) * np.cos(Y * scale)
        + np.sin(Y * scale / 2) * np.cos(X * scale / 2)
    )
    noise = coherence_amplitude * np.random.randn(grid_size, grid_size)
    return field + noise

def plot_field(field, title="QIR Cosmic Web Variation"):
    plt.figure(figsize=(8, 6))
    plt.imshow(field, cmap='inferno', origin='lower')
    plt.colorbar(label='Information Density')
    plt.title(title)
    plt.xlabel("X (arbitrary)")
    plt.ylabel("Y (arbitrary)")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    density = generate_density_field(grid_size=200, scale=12, coherence_amplitude=0.004)
    plot_field(density)
