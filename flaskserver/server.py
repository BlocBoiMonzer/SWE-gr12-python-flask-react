from flask import Flask, render_template, url_for, request, redirect, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
app.secret_key = "hadi"

# Read Members API route
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3", "Member4", "Ali", "Hadi"]}


# Begynn med å lage en funksjon for å legge til members

@app.route("/select_tours")
def select_tours():
    return render_template("select_tours.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        session["user"] = user
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


if __name__ == "__main__":
    app.run(debug=True)