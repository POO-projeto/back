from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_smorest import Api
from flask_cors import CORS
from dotenv import load_dotenv
import os
from authlib.integrations.flask_client import OAuth
from utils.functions.register_blueprints import register_blueprints
from config import db

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["API_TITLE"] = "DAILYTASK REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
app.config["OAUTHLIB_INSECURE_TRANSPORT"] = True
app.config["OAUTHLIB_RELAX_TOKEN_SCOPE"] = True
app.config["API_SPEC_OPTIONS"] = {
    "security": [{"bearerAuth": []}],
    "components": {
        "securitySchemes": {
            "bearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
        }
    },
}
db.init_app(app)
CORS(
    app,
    origins=[str(os.getenv("FRONTEND_URL"))],
)
migrate = Migrate(app, db)
api = Api(app)
register_blueprints(api)

oauth = OAuth(app)

google = oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url="https://accounts.google.com/o/oauth2/token",
    access_token_params=None,
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    authorize_params=None,
    userinfo_endpoint="https://www.googleapis.com/oauth2/v1/userinfo",
    client_kwargs={"scope": "openid profile email"},
)

from models import *

if __name__ == "__main__":
    app.run(debug=True)
