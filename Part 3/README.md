# TOPSIS Web Service (Part-III)  
**Author:** Ishita Singh Oberoi  
**Roll Number:** 102317272  

---

## Overview  

This project implements a **web-based TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** service using **Streamlit**.  

Users can:

- Upload a CSV dataset  
- Enter weights and impacts  
- Provide an email address  
- Receive ranked TOPSIS results via email  

The system processes the uploaded data, computes TOPSIS scores, and sends the result file to the user.

---

## Requirements  

- Python 3.x  
- Internet connection (for email sending)

Install dependencies:

```bash
pip install streamlit pandas numpy
```

---

## Project Structure  

```
Part3/
 ├ app.py
 ├ topsis.py
 ├ requirements.txt
 └ uploads/
```

---

## Run Locally  

Open terminal inside **Part3** folder and run:

```bash
python -m streamlit run app.py
```

The application will start at:

```
http://localhost:8501
```

Open this URL in your browser.

---

## Usage  

1. Upload a CSV file containing alternatives and criteria  
2. Enter weights (comma-separated numbers)  
3. Enter impacts (`+` for benefit, `-` for cost)  
4. Enter email address  
5. Click **Run TOPSIS**  

The computed result will be emailed as `result.csv`.

---

## Input File Format  

- First column → alternative names  
- Remaining columns → numeric criteria  
- Minimum 3 columns required  

Example:

```csv
Fund,P1,P2,P3,P4,P5
M1,0.67,0.45,65,42.6,12.56
M2,0.60,0.36,53,33.3,14.47
M3,0.82,0.67,48,63.1,17.10
M4,0.73,0.58,56,59.2,18.42
```

---

## Methodology  

The web service performs standard TOPSIS steps:

1. Normalize decision matrix  
2. Apply weights  
3. Determine ideal best and worst  
4. Compute distances  
5. Calculate TOPSIS score  
6. Rank alternatives  

---

## Email Functionality  

The application uses SMTP to send results to the user-provided email.  
An app password is required for the sender Gmail account.

---


