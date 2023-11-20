from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import timedelta

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "hadi"
app.permanent_session_lifetime = timedelta(days=5)

db = SQLAlchemy(app)
migrate = Migrate(app, db)



class users(db.Model):
    id = db.Column("Id", db.Integer, primary_key=True)
    firstname = db.Column("firstName", db.String(50))
    lastname = db.Column("lastName", db.String(50))
    phonenumber = db.Column("phoneNumber", db.Integer, unique=True, nullable=False)
    address = db.Column("address", db.String(100))
    email = db.Column("email", db.String(100), unique=True, nullable=False)
    username = db.Column("username", db.String(50), unique=True, nullable=False)
    password = db.Column("password", db.String(100), nullable=False)

    def __init__(self, firstname, lastname, phonenumber, address, email, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber
        self.address = address
        self.email = email
        self.username = username
        self.password = password



@app.route("/tours")
def select_tours():
    return render_template("tours.html")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        phonenumber = request.form["phonenumber"]
        address = request.form["address"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        if users.query.filter_by(email=email).first():
            flash("Email is already registered. Please choose a different email.")
            return redirect(url_for("register"))

        user = users(firstname=firstname, lastname=lastname, phonenumber=phonenumber, address=address,
                     email=email, username=username, password=password)

        db.session.add(user)
        db.session.commit()

        flash("Registration successful! You can now log in.")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/user")
def user():
    if "user" in session:
        return render_template("user.html", user=session["user"])
    else:
        flash("Du er ikke logget inn!")
        return redirect(url_for("login"))




@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        username = request.form["username"]
        password = request.form["password"]
        user = users.query.filter_by(username=username, password=password).first()

        if user:
            session["user"] = username
            return redirect(url_for("user"))
        else:
            flash("Feil brukernavn eller passord. Prøv igjen.", "error")
            return redirect(url_for("login"))
    else:
        if "user" in session:
            flash("Allerede logget inn!")
            return redirect(url_for("user"))

        return render_template("login.html")


@app.route("/register_user", methods=["POST", "GET"])
def register_user():
    if request.method == "POST":
        # Logikk for å registrere en ny bruker
        # ...
        return redirect(url_for("register_user"))  # Omdiriger tilbake til registreringssiden
    return render_template("register.html")


@app.route("/logout", methods=["POST", "GET"])
def logout():
    session.pop("user", None)
    session.pop("email", None)
    flash("Du har blitt logget ut", "info")
    return redirect(url_for("login"))

@app.route("/create_tour", methods=["POST"])
def create_tour():
    if request.method == "POST":
        destination = request.form.get("destination")
        date = request.form.get("date")
        description = request.form.get("description")
        flash("Reisen til {} er blitt opprettet!".format(destination))

        return redirect(url_for('tours'))  # Erstatt 'tours_page' med riktig rute for å vise reiser

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=3000)