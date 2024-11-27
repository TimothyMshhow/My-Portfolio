import datetime
import smtplib
from flask import Flask, render_template, request
import os

current_year = datetime.datetime.now()

my_email = os.environ.get('My_email')
my_pass = os.environ.get('Email_pass')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        user = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(from_addr=email, to_addrs="bigt.tm@protonmail.com",
                                msg=f"Subject:New message from you blog users!"
                                f"\n\nName: {user}\nEmail: {email}\n Message:{message}")
            return render_template("index.html", year=current_year.year, msg_sent=True)
    return render_template("index.html", year=current_year.year, msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
