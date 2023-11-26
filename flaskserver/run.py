from app import create_app, db
from routes import create_admin_user

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        create_admin_user()
    app.run(debug=True, port=3000)