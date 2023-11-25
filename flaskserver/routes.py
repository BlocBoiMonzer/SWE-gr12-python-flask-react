from flask import Blueprint, render_template, url_for, request, redirect, session, flash
from flask_login import current_user, login_required
from models import User, Booking, Tour
from datetime import datetime
from extensions import db
from werkzeug.utils import secure_filename
import os
from flask import current_app
from config import Config

main = Blueprint('main', __name__)

UPLOAD_FOLDER = os.path.join('flaskserver', 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}



@main.route("/")
def home():
    return render_template("index.html")


@main.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        phonenumber = request.form["phonenumber"]
        address = request.form["address"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        
        user = User.query.filter_by(username=username).first()
        if user:
            flash("Username is already taken. Please choose a different username.")
            return redirect(url_for("main.register"))

        if User.query.filter_by(email=email).first():
            flash("Email is already registered. Please choose a different email.")
            return redirect(url_for("main.register"))

        user = User(firstname=firstname, lastname=lastname, phonenumber=phonenumber, address=address,
                     email=email, username=username, password=password)

        db.session.add(user)
        db.session.commit()

        flash("Registration successful! You can now log in.")
        return redirect(url_for("main.login"))

    return render_template("register.html")

@main.route('/user', methods=['GET', 'POST'])
def user():
    if 'user' not in session:
        flash('Ikke innlogget.')
        return redirect(url_for("main.login"))

    current_user = User.query.filter_by(username=session['user']).first()
    if not current_user:
        flash('Kunne ikke finne brukeren.')
        return redirect(url_for("main.login"))

    if request.method == 'POST':
        try:
            current_user.firstname = request.form.get('firstname', '').strip()
            current_user.lastname = request.form.get('lastname', '').strip()
            db.session.commit()
            flash('Brukerinformasjon oppdatert.')
        except KeyError as e:
            flash(f'Manglende felt: {e}')
    return render_template('user.html', user=current_user)

@main.route('/user/update', methods=['POST'])
def update_user():
    if 'user' in session:
        current_user = User.query.filter_by(username=session['user']).first()
        if current_user:
            current_user.firstname = request.form['firstname']
            current_user.lastname = request.form['lastname']
            current_user.email = request.form['email']
            db.session.commit()
            flash('Brukerinformasjon oppdatert.')
            return redirect(url_for('main.user'))
        else:
            flash('Kunne ikke finne brukeren.')
            return redirect(url_for("main.login"))
    flash('Ikke innlogget.')
    return redirect(url_for("main.login"))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/upload_image', methods=['POST'])
def upload_image():
    if 'user' not in session:
        flash('Vennligst logg inn for å laste opp et bilde.')
        return redirect(url_for("main.login"))

    current_user = User.query.filter_by(username=session['user']).first()
    if current_user is None:
        flash('Noe gikk galt, kunne ikke finne bruker.')
        return redirect(url_for("main.login"))

    if 'image' not in request.files:
        flash('Ingen fil ble valgt.')
        return redirect(request.url)

    file = request.files['image']
    if file.filename == '':
        flash('Ingen fil ble valgt.')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        current_user.image_filename = filename
        db.session.commit()
        flash('Profilbilde er oppdatert.')
        return redirect(url_for('main.user'))

    flash('Opplasting mislyktes.')
    return redirect(url_for('main.user'))

@main.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


@main.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session["user"] = username
            flash("Du har blitt logget inn!")
            return redirect(url_for("main.user")) 

        else:
            flash("Feil brukernavn eller passord. Prøv igjen.", "error")
            return redirect(url_for("main.login"))

    return render_template("login.html")

@main.route("/index")
def logout():
    session.pop("user", None)
    session.pop("email", None)
    flash("Du har blitt logget ut", "info")
    return redirect(url_for("main.login"))

@main.route('/tours')
def show_tours():
    if 'user' not in session:
        flash('Vennligst logg inn for å se reiser.')
        return redirect(url_for('login'))
    tours = Tour.query.all()
    return render_template('tours.html', tours=tours)



current_path = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(current_path, 'static', 'uploads')

@main.route('/create_tour', methods=['GET', 'POST'])
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
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)
            image.save(os.path.join(UPLOAD_FOLDER, filename))
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

@main.route('/book-tour/<int:tour_id>', methods=['GET', 'POST'])
def book_tour(tour_id):
    if 'user' not in session:
        flash('Vennligst logg inn for å booke reiser.')
        return redirect(url_for("main.login"))

    tour = Tour.query.get_or_404(tour_id)
    current_user = User.query.filter_by(username=session['user']).first()

    if tour.host_id == current_user.id:
        flash('Du kan ikke booke din egen tur.')
        return redirect(url_for('main.show_tours'))

    if request.method == 'POST':
        existing_booking = Booking.query.filter_by(user_id=current_user.id, tour_id=tour.id).first()
        if existing_booking:
            flash('Du har allerede booket denne turen.')
            return redirect(url_for('main.show_tours'))
        new_booking = Booking(user_id=current_user.id, tour_id=tour.id)
        db.session.add(new_booking)
        db.session.commit()
        flash('Turen har blitt booket.')
        return redirect(url_for('main.user_bookings'))

    return render_template('main.book_tour', tour=tour)

@main.route('/my-bookings')
def user_bookings():
    if 'user' not in session:
        flash('Vennligst logg inn for å se dine bookinger.')
        return redirect(url_for("main.login"))

    current_user = User.query.filter_by(username=session['user']).first()
    if current_user is None:
        flash('Noe gikk galt, kunne ikke finne bruker.')
        return redirect(url_for("main.login"))

    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('main.my_bookings', bookings=bookings)