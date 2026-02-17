# TOPSIS Python Package  
**Author:** Ishita Singh Oberoi  
**Roll Number:** 102317272  

---

## Overview  

This project implements the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method in Python and publishes it as a reusable package on PyPI.  

TOPSIS is a multi-criteria decision-making technique used to rank alternatives based on their distance from an ideal best and ideal worst solution.  

The package allows users to compute TOPSIS scores and rankings directly from the command line using an input CSV dataset, weights, and impacts.

---

## PyPI Package  

**Latest Version (v0.3):**  
https://pypi.org/project/Topsis-Ishita-102317272/0.3/

**Project Page:**  
https://pypi.org/project/Topsis-Ishita-102317272/

---

## Installation  

Install the package from PyPI:

```bash
pip install --upgrade Topsis-Ishita-102317272
```

Verify installation:

```bash
pip show Topsis-Ishita-102317272
```

---

## Input File Format  

The input must be a CSV file with:

- First column → alternative names  
- Remaining columns → numeric criteria  
- At least 3 columns total  

Example:

```csv
Fund,P1,P2,P3,P4,P5
M1,0.67,0.45,65,42.6,12.56
M2,0.60,0.36,53,33.3,14.47
M3,0.82,0.67,48,63.1,17.10
M4,0.73,0.58,56,59.2,18.42
```

---

## Usage  

Run TOPSIS from command line:

```bash
topsis data.csv "1,1,1,1,1" "+,+,+,+,+" result.csv
```

Parameters:

- `data.csv` → input dataset  
- weights → comma-separated numeric values  
- impacts → `+` (benefit) or `-` (cost)  
- `result.csv` → output file  

---

## Output  

The output CSV contains:

- Original data  
- Topsis Score  
- Rank  

Example columns:

```
Fund,P1,P2,P3,P4,P5,Topsis Score,Rank
```

Higher TOPSIS score indicates better alternative.

---

## Methodology  

The package implements the standard TOPSIS steps:

1. Decision matrix normalization  
2. Weight application  
3. Ideal best and worst determination  
4. Distance calculation  
5. TOPSIS score computation  
6. Ranking of alternatives  

---

## Package Structure  

```
Part2/
 ├ topsis_ishita_102317272/
 │   ├ __init__.py
 │   └ topsis.py
 ├ setup.py
 └ README.md
```

---

## Features  

- Command-line interface  
- CSV input/output  
- Automatic validation  
- PyPI installable package  
- Cross-platform support  

---


