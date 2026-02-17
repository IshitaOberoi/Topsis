import streamlit as st
import os
import pandas as pd
from topsis import run_topsis
import smtplib
from email.message import EmailMessage

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def send_email(receiver, file_path):
    sender = "ishitaoberoi2005@gmail.com"
    password = "eekebugmicnjritq"

    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Your TOPSIS result is attached.")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="result.csv"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)


st.title("TOPSIS Web Service")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
weights = st.text_input("Weights (comma separated)", "1,1,1,1,1")
impacts = st.text_input("Impacts (+ or -)", "+,+,+,+,+")
email = st.text_input("Email")

if st.button("Run TOPSIS"):
    if uploaded_file is None or email == "":
        st.error("Please provide file and email")
    else:
        input_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        output_path = os.path.join(UPLOAD_FOLDER, "result.csv")

        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        run_topsis(input_path, weights, impacts, output_path)
        send_email(email, output_path)

        st.success("Result sent to email!")
