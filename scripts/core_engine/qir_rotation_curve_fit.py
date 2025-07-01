

"""
QIR Galaxy Rotation Curve Fit
Author: Christopher Patrick Booth Smolen, AXVIAM PBC
Purpose: Predict galactic rotation curves from memory-based curvature without dark matter.
"""

import numpy as np
import matplotlib.pyplot as plt
from .memory_function_phase import I_phase
from .qir_curvature_model import qir_curvature

def predict_velocity(r, M, D, a=1.0, b=0.7, T=200, G=6.67430e-11):
    """
    Predict rotational velocity at radius r using QIR-modified curvature.

    Parameters:
    - r: Radial distance from galactic center (m)
    - M: Galaxy mass interior to radius r (kg)
    - D: Distance to galaxy (m)
    - a: Scale parameter
    - b: Coupling coefficient
    - T: Structural phase time (default 200)
    - G: Gravitational constant

    Returns:
    - v: Rotational velocity at radius r (m/s)
    """
    I = I_phase(T)
    curvature = qir_curvature(M, a, D, b, I)
    v = np.sqrt(r * curvature)
    return v

def generate_rotation_curve(r_array, M_profile, D, a=1.0, b=0.7, T=200):
    """
    Generate full QIR-based rotation curve.

    Parameters:
    - r_array: array of radial distances (m)
    - M_profile: array of enclosed masses at each r (kg)
    - D: Distance to galaxy (m)

    Returns:
    - velocities: array of predicted velocities (m/s)
    """
    velocities = []
    for r, M in zip(r_array, M_profile):
        v = predict_velocity(r, M, D, a=a, b=b, T=T)
        velocities.append(v)
    return np.array(velocities)

# Example test plot
if __name__ == "__main__":
    r_kpc = np.linspace(0.1, 20, 100)
    r_m = r_kpc * 3.086e19  # convert kpc to meters
    M_profile = 1e40 * (r_kpc / r_kpc[-1])  # linear mass distribution

    D = 1e23  # m (approx. 3.2 Mpc)

    v_qir = generate_rotation_curve(r_m, M_profile, D)

    plt.plot(r_kpc, v_qir, label="QIR Predicted Velocity")
    plt.xlabel("Radius (kpc)")
    plt.ylabel("Velocity (m/s)")
    plt.title("QIR Rotation Curve Prediction")
    plt.legend()
    plt.grid(True)
    plt.show()
