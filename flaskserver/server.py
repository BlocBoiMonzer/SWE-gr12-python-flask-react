from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_cors import CORS
from datetime import timedelta

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
app.secret_key = "hadi"
app.permanent_session_lifetime = timedelta(days=5)

# Read Members API route
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3", "Member4", "Ali", "Hadi"]}


# Begynn med å lage en funksjon for å legge til members

@app.route("/select_tours")
def select_tours():
    return render_template("selecttours.html")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["username"]
        session["user"] = user
        flash("you have been logged inn!", "info")
        return redirect(url_for("user"))
    else:
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("you have been logged out!", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)