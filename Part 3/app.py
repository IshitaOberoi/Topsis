from flask import Flask, render_template, request, send_file
import os
from topsis import run_topsis
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def send_email(receiver, file_path):
    sender = "YOUR_EMAIL@gmail.com"
    password = "YOUR_APP_PASSWORD"

    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Your TOPSIS result is attached.")

    with open(file_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename="result.csv")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]
        email = request.form["email"]

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(UPLOAD_FOLDER, "result.csv")

        file.save(input_path)

        run_topsis(input_path, weights, impacts, output_path)

        send_email(email, output_path)

        return "Result sent to email!"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
