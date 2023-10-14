from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Read Members API route
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3", "Member4", "Ali", "Hadi"]}


# Begynn med å lage en funksjon for å legge til members


if __name__ == "__main__":
    app.run(debug=True)