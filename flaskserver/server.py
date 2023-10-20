from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_cors import CORS
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
app.secret_key = "hadi"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(days=5)


# Read Members API route
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3", "Member4", "Ali", "Hadi"]}

# Begynn med å lage en funksjon for å legge til members

db = SQLAlchemy(app)

class users(db.Model):
    

@app.route("/select_tours")
def select_tours():
    return render_template("selecttours.html")


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["username"]
        session["user"] = user
        flash("you have been logged inn!", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))

        return render_template("login.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email, user=user)
    else:
        flash("you are not logged in!")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("email", None)
    flash("you have been logged out!", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)