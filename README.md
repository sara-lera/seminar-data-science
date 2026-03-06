# Seminar Assignment: The Scientific Paper of the Future (UPM)

[PLACEHOLDER: AQUÍ PEGARÁS EL BADGE DE ZENODO DESPUÉS DEL RELEASE]

## Description
This repository named `seminar-data-science` is the practical assignment for the "Scientific Paper of the Future" seminar. It contains a simple Python script as an example of software and a schema of the provenance of the use-case described in exercise 2. The objective is to follow best practices in open science, software metadata, and research provenance.

## Overview
The repository is organized into two main parts:
1. **Exercise 1:** A Python-based tool for statistical analysis, including metadata, persistent identification and license.
2. **Exercise 2:** A provenance record of a research lifecycle using the W3C PROV standard.

## 1. Software and Metadata (Exercise 1)
This section aims to make research software Findable, Accessible, Interoperable, and Reusable (FAIR).

### Included Files:
* **`t_test_example.py`**: A Python script that generates synthetic data for two groups, calculates the t-statistic and p-value, and determines if the null hypothesis is rejected based on a 0.05 significance level.
* **`codemeta.json`**: A metadata file following the CodeMeta standard to describe software authorship, dependencies, and features in an interoperable way.
* **`LICENSE`**: An Apache 2.0 license file defining the legal permissions for the use, modification, and distribution of the code.

### Installation & usage 
Ensure you have Python 3 installed. You will need the following libraries:
```bash
pip install numpy scipy
python t_test_example.py
```
### How to Cite
If you use this software or the provenance diagram in your research, please cite it as follows:

Lera, Sara. (2026). **Data Science Seminar Assignment**. (Version 1.0.0). Universidad Politécnica de Madrid. GitHub. doi de zenodo. 
