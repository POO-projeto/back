from dotenv import load_dotenv
import jwt
import os

load_dotenv()


def decode_jwt(token):
    try:
        decoded = jwt.decode(token, str(os.getenv("SECRET_KEY")), algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
