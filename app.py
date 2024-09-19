from model.database import db
from flask import Flask
from flask import Flask,jsonify,redirect,url_for,request
from flask_migrate import Migrate
from model.User_db import Student
from model.Login_db import StudentLogin
from endpoints.User import student_bp
from endpoints.StudentLogin import student_login_bp


app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(student_bp, url_prefix='/student/')
app.register_blueprint(student_login_bp,url_prefix='/studentLogin')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)