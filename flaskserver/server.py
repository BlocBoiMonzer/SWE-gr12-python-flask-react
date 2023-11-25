from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import timedelta, datetime
import os
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = os.path.join('static', 'uploads')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
CORS(app)
app.secret_key = "hadi"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "hadi"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=5)
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)




class users(db.Model):
    ID = db.Column("ID", db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column("firstName", db.String(50))
    lastname = db.Column("lastName", db.String(50))
    phonenumber = db.Column("phoneNumber", db.Integer)
    address = db.Column("address", db.String(100))
    email = db.Column("email", db.String(100))
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




@app.route('/user', methods=['GET', 'POST'])
def user():
    if 'user' not in session:
        flash('Ikke innlogget.')
        return redirect(url_for('login'))

    current_user = users.query.filter_by(username=session['user']).first()
    if not current_user:
        flash('Kunne ikke finne brukeren.')
        return redirect(url_for('login'))

    if request.method == 'POST':
        try:
            current_user.firstname = request.form.get('firstname', '').strip()
            current_user.lastname = request.form.get('lastname', '').strip()
            db.session.commit()
            flash('Brukerinformasjon oppdatert.')
        except KeyError as e:
            flash(f'Manglende felt: {e}')
    return render_template('user.html', user=current_user)



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/user/update', methods=['POST'])
def update_user():
    if 'user' in session:
        current_user = users.query.filter_by(username=session['user']).first()
        if current_user:
            current_user.firstname = request.form['firstname']
            current_user.lastname = request.form['lastname']
            current_user.email = request.form['email']
            db.session.commit()
            flash('Brukerinformasjon oppdatert.')
            return redirect(url_for('user'))
        else:
            flash('Kunne ikke finne brukeren.')
            return redirect(url_for('login'))
    flash('Ikke innlogget.')
    return redirect(url_for('login'))


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image successfully uploaded and displayed below')
        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        username = request.form["username"]
        password = request.form["password"]
        user = users.query.filter_by(username=username, password=password).first()

        if user:
            session["user"] = username
            flash("Du har blitt logget inn!")
            return redirect(url_for("index"))

        else:
            flash("Feil brukernavn eller passord. Prøv igjen.", "error")
            return redirect(url_for("index"))
    else:
        if "user" in session:
            flash("Allerede logget inn!")
            return redirect(url_for("login"))

        return render_template("login.html")


@app.route("/index")
def logout():
    session.pop("user", None)
    session.pop("email", None)
    flash("Du har blitt logget ut", "info")
    return redirect(url_for("login"))


@app.route('/tours')
def show_tours():
    if 'user' not in session:
        flash('Vennligst logg inn for å se reiser.')
        return redirect(url_for('login'))
    tours = Tour.query.all()
    return render_template('tours.html', tours=tours)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.id'), nullable=False)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.ID'))
    user = db.relationship('users', backref='user_bookings')
    tour = db.relationship('Tour', backref='tour_bookings')


class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)


@app.route('/create_tour', methods=['GET', 'POST'])
def create_tour():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        start_date_str = request.form.get('start_date')
        end_date_str = request.form.get('end_date')
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        image = request.files['image']
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_url = 'uploads/' + filename
        else:
            flash('Tillatte bildetyper er - png, jpg, jpeg, gif')
            return redirect(request.url)

        new_tour = Tour(
            name=name,
            description=description,
            price=price,
            start_date=start_date,
            end_date=end_date,
            image_url=image_url
        )

        db.session.add(new_tour)
        db.session.commit()
        return redirect(url_for('show_tours'))
    return render_template('create_tour.html')


def create_tour_form():
    if 'user' not in session:
        flash('Vennligst logg inn for å opprette reiser.')
        return redirect(url_for('login'))
    return render_template('create_tour.html')


@app.route('/book-tour/<int:tour_id>', methods=['GET', 'POST'])
def book_tour(tour_id):
    if 'user' not in session:
        flash('Vennligst logg inn for å booke reiser.')
        return redirect(url_for('login'))

    tour = Tour.query.get_or_404(tour_id)
    current_user = users.query.filter_by(username=session['user']).first()

    if request.method == 'POST':
        existing_booking = Booking.query.filter_by(user_id=current_user.id, tour_id=tour.id).first()
        if existing_booking:
            flash('Du har allerede booket denne turen.')
            return redirect(url_for('show_tours'))
        new_booking = Booking(user_id=current_user.id, tour_id=tour.id)
        db.session.add(new_booking)
        db.session.commit()
        flash('Turen har blitt booket.')
        return redirect(url_for('user_bookings'))

    return render_template('book_tour.html', tour=tour)


@app.route('/my-bookings')
def user_bookings():
    if 'user' not in session:
        flash('Vennligst logg inn for å se dine bookinger.')
        return redirect(url_for('login'))

    current_user = users.query.filter_by(username=session['user']).first()
    if current_user is None:
        flash('Noe gikk galt, kunne ikke finne bruker.')
        return redirect(url_for('login'))

    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('my_bookings.html', bookings=bookings)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=3000)