# Implements a registration form using a select menu

from flask import Flask, render_template, request

app = Flask(__name__)

WEATHER = [
    "Current Weather",
    "Hourly Weather",
    "7 Day forecast"
]


@app.route("/")
def index():
    return render_template("index.html", forecasts=WEATHER)


@app.route("/register", methods=["POST"])
def register():

    # Validate submission
    if not request.form.get("name") or request.form.get("forecast") not in WEATHER:
        return render_template("failure.html")

    # Confirm registration
    return render_template("success.html")