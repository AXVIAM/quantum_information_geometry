

"""
Compare QIR vs GR Lensing Predictions
Author: Christopher Patrick Booth Smolen, AXVIAM PBC
Purpose: Compare gravitational lensing predictions from General Relativity and QIR across systems.
"""

import numpy as np
from ..core_engine.qir_predict_lensing import predict_lensing_angle

def arcsec(radians):
    return radians * (180 / np.pi) * 3600

def compare_system(M, D, name, use_I_model=True, t=200):
    theta_qir, theta_gr, I = predict_lensing_angle(M, D, use_I_model=use_I_model, t=t)
    return {
        "system": name,
        "mass (kg)": M,
        "distance (m)": D,
        "I": round(I, 6),
        "theta_GR_arcsec": round(arcsec(theta_gr), 6),
        "theta_QIR_arcsec": round(arcsec(theta_qir), 6),
        "delta_arcsec": round(arcsec(theta_qir - theta_gr), 6)
    }

if __name__ == "__main__":
    systems = [
        {"name": "UGC00128", "M": 2.3e41, "D": 2.5e23},
        {"name": "NGC3198", "M": 4.5e41, "D": 3.1e23},
        {"name": "NGC2403", "M": 3.2e41, "D": 2.9e23},
        {"name": "SDSS J0737+3216", "M": 1.4e42, "D": 1.1e25},
        {"name": "SDSS J1430+4105", "M": 1.2e42, "D": 1.0e25}
    ]

    print("QIR vs GR Lensing Comparison:")
    for s in systems:
        result = compare_system(s["M"], s["D"], s["name"])
        print(result)
