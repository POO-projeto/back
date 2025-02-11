from flask import Blueprint, make_response, jsonify, session, request, redirect, g
from config import db
from models import User
from utils.decorators.is_logged_in import is_logged_in
from utils.decorators.is_not_logged_in import is_not_logged_in

import requests
from dotenv import load_dotenv
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import os
import pathlib
import google.auth.transport.requests
import jwt
from flask_smorest import Blueprint
from sqlalchemy.exc import SQLAlchemyError
from config import GOOGLE_CLIENT_ID, BACKEND_URL, FRONTEND_URL, secret_key
from utils.functions.get_logged_in_user import get_logged_in_user

load_dotenv()

blp = Blueprint(
    "Google Auth", __name__, description="OAuth via Google", url_prefix="/auth"
)

client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=[
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/userinfo.email",
        "openid",
    ],
    redirect_uri=str(BACKEND_URL) + "/auth/callback",
)


def generate_jwt(payload):
    encoded_jwt = jwt.encode(payload, key=str(secret_key), algorithm="HS256")
    return encoded_jwt


@blp.route("/login", methods=["GET"])
@is_not_logged_in
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state

    return (
        jsonify({"message": "Login initiated", "authorization_url": authorization_url}),
        200,
    )


@blp.route("/callback", methods=["GET"])
def callback():
    flow.fetch_token(authorization_response=request.url)
    credentials = flow.credentials
    request_session = requests.session()
    token_request = google.auth.transport.requests.Request(session=request_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token, request=token_request, audience=GOOGLE_CLIENT_ID
    )
    g.google_id = id_info.get("sub")

    user = User.query.filter_by(email=id_info.get("email")).first()
    print(user)
    if user is None:
        user = User(
            name=id_info.get("given_name"),
            email=id_info.get("email"),
            photo=id_info.get("picture"),
        )
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError as error:
            return jsonify({"message": "Database error", "error_code": str(error)}), 500

    session_user = {
        "id": user.id,
        "name": id_info.get("given_name"),
        "email": id_info.get("email"),
        "photo": id_info.get("picture"),
    }
    jwt_token = generate_jwt(session_user)
    del id_info["aud"]
    jwt_token = generate_jwt(session_user)

    response = make_response(redirect(f"{FRONTEND_URL}?jwt={jwt_token}"))

    return response


@blp.route("/info", methods=["GET"])
@is_logged_in
def info():
    user_data = jwt.decode(
        str(request.headers.get("Authorization")).split(" ")[1],
        algorithms=["HS256"],
        key=str(secret_key),
    )
    user = User.query.filter_by(email=user_data["email"]).first()
    if not user:
        return jsonify({"message": "Usuário não encontrado."})
    user_data["id"] = user.id
    return jsonify(user_data), 200
