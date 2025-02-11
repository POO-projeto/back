from functools import wraps
from flask import request, jsonify, g
import jwt
from config import secret_key


def is_logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            token = auth_header.split(" ")[1]
            decoded_token = jwt.decode(token, str(secret_key), algorithms=["HS256"])

            g.user = decoded_token
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 401

        return f(*args, **kwargs)

    return decorated_function
