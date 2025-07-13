# AXVIAM Quantum Information Geometry (QIR Engine)

**Author:** Christopher Patrick Booth Smolen  
**Affiliation:** AXVIAM PBC  
**License:** Apache 2.0  
**Repository:** [https://github.com/axviam/quantum-information-geometry](https://github.com/axviam/quantum-information-geometry)

---

## 🧠 Overview

General Relativity describes how mass curves spacetime — but fails to explain certain gravitational phenomena without invoking dark matter or energy. QIR offers a testable alternative: curvature emerges from the coherence of a system’s structural memory, derived from first principles.

This repository presents the full implementation of **Quantum Information Geometry (QIR)** — a model that explains spacetime curvature as the result of a system’s memory of transformation (its internal structural coherence), rather than mass alone. In regions where General Relativity cannot match observation using visible matter, QIR uses measurable information coherence to predict curvature from the system’s formation history.

---

## 🧪 Core Capabilities

- ✅ Predicts gravitational lensing without dark matter  
- ✅ Matches observed galactic rotation curves  
- ✅ Models black hole entropy from memory structure  
- ✅ Simulates cosmic web formation via information flow  
- ✅ Supports structure formation growth equations  
- ✅ Reconstructs cosmological expansion without dark energy  

---

## 📂 Repository Structure

```text
/core_engine
    qir_curvature_model.py         - QIR curvature equation
    memory_function_phase.py       - Harmonic coherence function I(t)
    qir_predict_lensing.py         - Light deflection calculator
    qir_rotation_curve_fit.py      - Predicts galactic rotation curves

/tests_and_data
    compare_qir_vs_gr.py           - GR vs QIR deflection comparison
    galaxy_loader.py               - Parses .dat and .csv galaxy inputs
    galaxy_data/                   - Galaxy rotation files (UGC00128, NGC2403, etc.)

/black_hole_modeling
    qir_black_hole_entropy.py      - Entropy with QIR memory correction
    black_hole_memory_curve.py     - Memory curve across BH radius
    gravitational_wave_feedback.py - Waveform echoes from memory feedback

/cosmic_structure
    cosmic_web_variations.py       - LSS simulation from memory fluctuations
    qig_cosmic_web_refined.py      - Phase-structured cosmic web emergence
    perturbation_qir_extension.py  - Growth equations under QIR

```

---

## 🔬 Reproducibility

All core predictions were verified using real galaxy data:

- **Rotation Curves**: UGC00128, NGC2403, NGC3198  
- **Lensing Systems**: SDSS J0737+3216, SDSS J1430+4105  

> 📌 Data and comparison results are provided in `/tests_and_data/lensing_comparison.csv`

QIR reproduces observed phenomena *without invoking dark matter or dark energy.*

---

## 📘 Documentation

The full theory, derivations, and observational results are published here:

📄 [QIR Engine Whitepaper (PDF)](https://doi.org/10.5281/zenodo.15779147)  
📄 Cover letter + summary: `cover_letter_intro_to_qir.txt`  
📄 Supplementary proofs and black hole framework: See `/docs` (if applicable)

---

## Installation

Install the Python dependencies and run from the repository root:

```bash
pip install -r requirements.txt
```


## 🚀 Running the Model

To compare predictions:

```bash
python3 -m scripts.tests_and_data.compare_qir_vs_gr
```

To visualize memory-driven cosmic structure:

```bash
python3 scripts/cosmic_structure/qig_cosmic_web_refined.py
```

To simulate black hole entropy:

```bash
python3 scripts/black_hole_modeling/qir_black_hole_entropy.py
```

---

## 📫 Citation

To cite this work:

```bibtex
Smolen, C.P.B. (2025). Quantum Information Geometry: A Memory-Based Foundation for Spacetime Curvature. Zenodo. https://doi.org/10.5281/zenodo.15779147
```

---

## 🤝 Contributing

This is an open and expanding foundation.  
Pull requests, issues, and community testing are welcomed.

---

## 💬 Contact

For correspondence: 
Christopher P. B. Smolen
**axviam@proton.me**  

