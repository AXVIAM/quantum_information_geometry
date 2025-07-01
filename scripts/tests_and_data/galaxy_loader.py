

"""
Galaxy Data Loader
Author: Christopher Patrick Booth Smolen, AXVIAM PBC
Purpose: Utility functions for loading and parsing galaxy rotation curve datasets.
"""

import numpy as np
import pandas as pd

def load_rotmod_file(filepath):
    """
    Load a galaxy rotation model data file (e.g. UGC00128_rotmod.dat).
    Assumes two-column format: radius (kpc), velocity (km/s)

    Returns:
    - radius_kpc: numpy array of radii in kiloparsecs
    - velocity_kms: numpy array of velocities in km/s
    """
    data = np.loadtxt(filepath)
    radius_kpc = data[:, 0]
    velocity_kms = data[:, 1]
    return radius_kpc, velocity_kms

def load_csv_lensing_data(filepath):
    """
    Load a CSV with QIR vs GR lensing comparisons.

    Returns:
    - pandas DataFrame
    """
    df = pd.read_csv(filepath)
    return df

# Example usage
if __name__ == "__main__":
    rot_path = "../galaxy_data/UGC00128_rotmod.dat"
    r, v = load_rotmod_file(rot_path)
    print(f"Loaded {len(r)} points from {rot_path}")
    print("First 5 radii (kpc):", r[:5])
    print("First 5 velocities (km/s):", v[:5])
