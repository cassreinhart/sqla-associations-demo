from flask_sqlalchemy import SQLALCHEMY_DATABASE_URI
# This line above generates an error...

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

#Models go below

class Department(db.Model):
    """Department. A department has many employees."""

    __tablename__ = "departments"

    dept_code = db.Column(db.Text, primary_key=True)
    dept_name = db.Column(db.Text, nullable=False, unique=True)
    phone = db.Column(db.Text)

class Employees(db.Model):
    """Employee Model"""

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    state = db.Column(db.Text, nullable=False, default='CA')
    # dept_code = db.Column(db.Text)