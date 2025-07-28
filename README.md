# Integrated Modeling of Point-Source Pollutants in Watersheds Using SWAT+

This repository contains the code and tools developed for the paper:

> [**Integrated modeling of the generation, attenuation, and transport of point-source pollutants at the watershed-scale using SWAT+**](https://www.sciencedirect.com/science/article/abs/pii/S1364815225003159)

<p align="center">
  <a href="https://www.sciencedirect.com/science/article/abs/pii/S1364815225003159">
    <img src="https://ars.els-cdn.com/content/image/1-s2.0-S1364815225003159-ga1_lrg.jpg" alt="Paper Thumbnail" width="500"/>
  </a>
</p>

## Summary

This modeling framework enables the simulation of pharmaceutical and industrial pollutants in river basins by combining expert-based pollutant generation with physically based watershed modeling using SWAT+. The framework consists of three integrated components:

1. **Pollutant Generation Model**  
   Built upon literature review and expert knowledge, this model simulates pollutant generation and removal in wastewater treatment plants (WWTPs) and industrial direct discharges.

2. **Attenuation and Transport Model**  
   An implementation based on SWAT+ in-stream routines that simulates the attenuation and transport of point-source pollutants in rivers and reservoirs.

3. **Coupling and Calibration with `pySWATPlus`**  
   A Python library that enables coupling of external models to SWAT+ and allows for joint simulation and calibration as a single integrated process.

---

## Components

### 🔹 [pySWATPlus](https://github.com/swat-model/pySWATPlus)

`pySWATPlus` is a Python library tailored for seamless interaction with the Soil and Water Assessment Tool Plus (SWAT+), empowering users to efficiently manage input and output files within Python environments. It is used for model execution, parameter editing, and data extraction.

---

### 🔹 [pollution_generation_model](https://github.com/icra/pollution_generation_model)

A model for estimating pollution from wastewater treatment plants (WWTPs) and industrial direct discharges in the CIC watershed region. It provides point-source pollutant loads that are used as inputs in SWAT+.

---

### 🔹 [SWATPollution](https://github.com/icra/pollution_generation_model)

The `SWATPollution` class is designed to manage the setup and optional execution of a SWAT+ simulation for modeling contaminant transport in a specified watershed. It facilitates input preparation, parameter configuration, and integration of observational data for analysis and calibration.

---

## How to Cite

If you use this code or any of its components in your work, please cite the following:

#### 📄 Main Paper

```bibtex
@article{SALOGRAU2025106631,
  title = {Integrated modeling of the generation, attenuation, and transport of point-source pollutants at the watershed-scale using SWAT+},
  journal = {Environmental Modelling & Software},
  pages = {106631},
  year = {2025},
  issn = {1364-8152},
  doi = {https://doi.org/10.1016/j.envsoft.2025.106631},
  url = {https://www.sciencedirect.com/science/article/pii/S1364815225003159},
  author = {Joan Saló-Grau and Laia Estrada and Oliu Llorente and Wolfgang Gernjak and Xavier Garcia and Natalja Čerkasova and Jeffrey G. Arnold and Vicenç Acuña},
  keywords = {water quality modeling, point-source pollution, wastewater treatment, pollutant attenuation, integrated modeling, calibration},
  abstract = {Addressing the chemical pollution of surface water bodies requires a good understanding of pollutant and system dynamics. Numerical modeling represents a valuable tool to support sustainable water management, especially due to its capacity to explore climate and management scenarios. We introduce a novel integrated modeling framework to capture the dynamics of point-source pollutants at the watershed-scale. It comprises a pollution generation model, an attenuation and transport model built within SWAT+, and a custom Python library (pySWATPlus) to facilitate model integration and calibration. We tested the framework for ciprofloxacin and venlafaxine in three densely populated Mediterranean basins, and we successfully calibrated it using observed concentrations in the river network. This research advances water quality modeling by integrating point-source pollutant dynamics from source to in-stream fate with the widely used model SWAT+. It also offers a valuable tool for evaluating mitigation strategies, supporting compliance with regulations, and informing sustainable water management.}
}
```

#### 🧩 pySWATPlus Library
```bibtex
@software{joan_salo_2025_16380058,
  author       = {Joan Saló and Debasish Pal and Oliu Llorente},
  title        = {swat-model/pySWATPlus: Release v1.0.1},
  month        = jul,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {v1.0.1},
  doi          = {10.5281/zenodo.16380058},
  url          = {https://doi.org/10.5281/zenodo.16380058},
  swhid        = {swh:1:dir:22ad2f4e620c3ef99bc62dd880cbc05c0be3c2b8;origin=https://doi.org/10.5281/zenodo.14889319;visit=swh:1:snp:4dc18853eb47c828caa36afd324ab58c8c8c02b2;anchor=swh:1:rel:c2e6bc6de431c7201ab6f484fc3096b43cb5a90e;path=swat-model-pySWATPlus-022f59a},
}
```
