

"""
QIR Gravitational Lensing Prediction
Author: Christopher Patrick Booth Smolen, AXVIAM PBC
Purpose: Predict angular deflection of light due to mass and information curvature using QIR.
"""

import numpy as np
from core_engine.memory_function_phase import I_phase
from core_engine.qir_curvature_model import qir_curvature

def predict_lensing_angle(M, D, I_val=None, alpha=0.000195, use_I_model=False, t=200):
    """
    Predict the total deflection angle using QIR.

    Parameters:
    - M: Mass (kg)
    - D: Distance (m)
    - I_val: Optional fixed coherence value. If None and use_I_model=True, uses I_phase(t)
    - alpha: Information curvature constant (empirically derived)
    - use_I_model: Whether to compute I using I_phase function
    - t: Time or structural scale input to I_phase if use_I_model=True

    Returns:
    - theta_qir: Angular deflection in radians (can convert to arcsec externally)
    """
    G = 6.67430e-11  # m^3 kg^-1 s^-2
    c = 3e8          # m/s

    # Standard GR deflection
    theta_gr = (4 * G * M) / (c**2 * D)

    # QIR information correction
    if use_I_model:
        I = I_phase(t)
    else:
        I = I_val if I_val is not None else 0.001

    theta_qir = theta_gr + alpha  # Simple QIR correction form
    return theta_qir, theta_gr, I

# Example
if __name__ == "__main__":
    M = 2e40  # kg
    D = 1e22  # m
    theta, theta_gr, I = predict_lensing_angle(M, D, use_I_model=True)
    print(f"QIR Lensing Deflection: {theta} radians")
    print(f"GR Deflection: {theta_gr} radians")
    print(f"Information Coherence I: {I}")