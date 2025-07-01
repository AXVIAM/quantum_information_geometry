

"""
QIR Memory Function Phase Model
Author: Christopher Patrick Booth Smolen, AXVIAM PBC
Purpose: Defines the time-phase structured memory field I(T) used in QIR curvature predictions.
"""

import numpy as np

def I_phase(t, pi=np.pi, A=1.0, T_scale=200):
    """
    Harmonic memory coherence function.

    Parameters:
    - t: Time or structural parameter (can be normalized)
    - pi: Pi constant (structural threshold of coherence)
    - A: Amplitude scaling of memory field
    - T_scale: Temporal phase-scaling constant (sets the memory wave structure)

    Returns:
    - I(t): Coherence memory intensity at time t
    """
    # Memory coherence wave (bounded by pi and phase-stabilized)
    memory = A * np.sin((pi * t) / T_scale) * np.exp(-t / T_scale)
    return memory

def memory_derivative(t, pi=np.pi, A=1.0, T_scale=200):
    """
    First derivative of I(t) with respect to time for dynamic feedback models.
    """
    dI = A * ((pi / T_scale) * np.cos((pi * t) / T_scale) - (1 / T_scale) * np.sin((pi * t) / T_scale)) * np.exp(-t / T_scale)
    return dI

# Example usage
if __name__ == "__main__":
    t_values = np.linspace(0, 1000, 500)
    I_values = I_phase(t_values)
    dI_values = memory_derivative(t_values)

    # Output preview (no plotting here, just verification)
    print(f"I(0) = {I_phase(0)}")
    print(f"I(200) = {I_phase(200)}")
    print(f"dI/dt at t=200 = {memory_derivative(200)}")
