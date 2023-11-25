from datetime import timedelta

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "hadi"
    PERMANENT_SESSION_LIFETIME = timedelta(days=5)
    UPLOAD_FOLDER = 'C:\\Users\\abdul\\OneDrive\\Documents\\software_engineering\\SWE-gr12-python-flask-react\\flaskserver\\static\\uploads'