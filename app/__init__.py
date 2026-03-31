from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
	load_dotenv()

	app = Flask(__name__)
	app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') #CHAVE FIXA DO .ENV
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/flask_crud'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


	db.init_app(app)

	login_manager = LoginManager()
	login_manager.init_app(app)
	login_manager.login_view = "main.login"

	from .routes import main
	app.register_blueprint(main)

	from . import models

	return app


