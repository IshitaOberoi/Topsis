# TOPSIS Command-Line Implementation (Part-I)  
**Author:** Ishita Singh Oberoi  
**Roll Number:** 102317272  

---

## Overview  

This project implements the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method as a standalone Python command-line program.  

TOPSIS is a multi-criteria decision-making technique used to rank alternatives based on their similarity to the ideal best and ideal worst solutions.  

The program reads a CSV dataset, applies weights and impacts to criteria, computes TOPSIS scores, and outputs ranked results in a new CSV file.

---

## Requirements  

- Python 3.x  
- pandas  
- numpy  

Install dependencies:

```bash
pip install pandas numpy
```

---

## Project Structure  

```
Part1/
 ├ data.csv
 └ topsis.py
```

---

## Input File Format  

The input must be a CSV file with:

- First column → alternative names  
- Remaining columns → numeric criteria values  
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

Run the TOPSIS program from the command line:

```bash
python topsis.py data.csv "1,1,1,1,1" "+,+,+,+,+" result.csv
```

Parameters:

- `data.csv` → input dataset  
- weights → comma-separated numeric values  
- impacts → `+` (benefit) or `-` (cost)  
- `result.csv` → output file  

---

## Output  

The program generates a CSV file containing:

- Original data  
- Topsis Score  
- Rank  

Example columns:

```
Fund,P1,P2,P3,P4,P5,Topsis Score,Rank
```

Higher TOPSIS score indicates a better alternative.

---

## Methodology  

The implementation follows standard TOPSIS steps:

1. Normalize the decision matrix  
2. Apply criterion weights  
3. Determine ideal best and ideal worst  
4. Compute separation distances  
5. Calculate TOPSIS scores  
6. Rank alternatives  

---

## Input Validation  

The program checks:

- Correct number of command-line parameters  
- Input file existence  
- Minimum number of columns  
- Numeric criteria values  
- Matching weights and impacts count  
- Valid impacts (`+` or `-`)  

---

