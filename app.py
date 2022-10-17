# Implements a registration form using a select menu

from flask import Flask, render_template, request

app = Flask(__name__)

if __name__=='__main__':
    app.run(debug=True)

WEATHER = [
    "Current Weather",
    "Hourly Weather",
    "7 Day forecast"
]


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html", forecasts=WEATHER)


@app.route("/register", methods=["POST"])
def register():

    # Validate submission
    if not request.form.get("location") or request.form.get("forecast") not in WEATHER:
        return render_template("failure.html")

    # Confirm registration
    return render_template("success.html")


@app.route("/current")
@app.route("/today")
def current():
    return render_template("current.html", forecasts=WEATHER)


@app.route("/hourly")
def hourly():
    return render_template("hourly.html", forecasts=WEATHER)


@app.route("/7day")
@app.route("/seven_day")
@app.route("/week")
@app.route("/weekly")
def seven_day():
    return render_template("7day.html", forecasts=WEATHER)