

"""
QIR-Based Cosmological Perturbation Growth
Author: Christopher Patrick Booth Smolen, AXVIAM PBC
Purpose: Extension of structure formation models using QIR's memory field influence on perturbation growth.
"""

import numpy as np
import matplotlib.pyplot as plt

def growth_factor_qir(a, I0=0.001, gamma=0.55, k=1.0):
    """
    Calculate perturbation growth factor D(a) under QIR-influenced dynamics.

    Parameters:
    - a: scale factor (array)
    - I0: baseline information coherence (structure memory term)
    - gamma: growth index (can vary under QIR)
    - k: memory coupling coefficient

    Returns:
    - D(a): perturbation growth factor
    """
    D = a**(1 + gamma * np.log(1 + k * I0 * a))
    return D

def plot_growth_comparison():
    a = np.linspace(0.01, 1.0, 200)
    D_gr = a  # linear GR growth
    D_qir = growth_factor_qir(a)

    plt.figure(figsize=(8, 6))
    plt.plot(a, D_gr, label="GR Growth (D ∝ a)", linestyle="--")
    plt.plot(a, D_qir, label="QIR Modified Growth", linewidth=2)
    plt.xlabel("Scale Factor a")
    plt.ylabel("Growth Factor D(a)")
    plt.title("Cosmological Perturbation Growth Under QIR")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_growth_comparison()