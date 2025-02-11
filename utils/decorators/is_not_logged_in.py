from functools import wraps
from flask import request, jsonify
import jwt
from config import secret_key


def is_not_logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if auth_header:
            try:
                token = auth_header.split(" ")[1]
                jwt.decode(token, key=str(secret_key), algorithms=["HS256"])
                return jsonify({"message": "You are already logged in."}), 403
            except jwt.ExpiredSignatureError:
                return (
                    jsonify({"message": "Token has expired. Please log in again."}),
                    401,
                )
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid token. Please log in."}), 401

        return f(*args, **kwargs)

    return decorated_function
