from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api
from dotenv import load_dotenv
import os
from utils.functions.register_blueprints import register_blueprints
from config import db


def create_app(db_url):
    load_dotenv()
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)
    register_blueprints(api)
    return app
