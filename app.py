from flask import Flask, render_template, request, redirect, url_for, session
import joblib
from functools import wraps

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret-key"  # required for sessions

# Load model
model = joblib.load("student_model.pth")

VALID_USERNAME = "admin"
VALID_PASSWORD = "12345678"


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated


@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("predictor_page"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("landing"))


@app.route("/predictor")
@login_required
def predictor_page():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
@login_required
def predict():
    cgpa = float(request.form["cgpa"])
    attendance = float(request.form["attendance"])

    prediction = model.predict([[cgpa, attendance]])[0]

    result = "PASS" if prediction == 1 else "FAIL"

    return render_template(
        "index.html",
        prediction=result,
        cgpa=cgpa,
        attendance=attendance
    )


if __name__ == "__main__":
    app.run(debug=True)