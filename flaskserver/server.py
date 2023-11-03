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
    id = db.Column("Id", db.Integer, primary_key=True)
    firstname = db.Column("FirstName", db.String(50))
    lastname = db.Column("LastName", db.String(50))
    phonenumber = db.Column("PhoneNumber", db.Integer)
    adresse = db.Column("Adresse", db.String(100))

    def __init__(self, id, firstname, lastname, phonenumber, adresse):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber
        self.adresse = adresse


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
        user_found = users.query.filter_by(id=user).first()
        if user_found:
            session["email"] = user_found.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()
        flash("you have been logged inn!")
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
            user_found = users.query.filter_by(id=user).first()
            user_found.email = email
            db.session.commit()
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
    db.create_all()
    app.run(debug=True)