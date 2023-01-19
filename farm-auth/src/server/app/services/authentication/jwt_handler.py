import time
from typing import Dict
import jwt
from app.config import Settings


secret_key = Settings().secret_key


class JWTHandler:

    def token_response(self, token: str):
        return {
            "access_token": token
        }

    def sign_jwt(self, user_id: str) -> Dict[str, str]:
        # Set the expiry time.
        payload = {
            'user_id': user_id,
            'expires': time.time() + 24000
        }
        return self.token_response(jwt.encode(payload, secret_key, algorithm="HS256"))


    def decode_jwt(token: str) -> dict:
        decoded_token = jwt.decode(token.encode(), secret_key, algorithms=["HS256"])
        return decoded_token if decoded_token['expires'] >= time.time() else {}



