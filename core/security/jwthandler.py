from datetime import datetime, timedelta
from core.exceptions.base import UnauthorizedException
from server.config import config
from jwt import decode, encode, ExpiredSignatureError, InvalidTokenError


class JWTHandler:
    secret_key = config.SECRET_KEY
    algorithm = "HS256"
    expire_refresh = timedelta(days=14)
    expire_access = timedelta(minutes=15)

    @staticmethod
    def encode(payload: dict, type_: str) -> str:
        if type_ == "access":
            t = JWTHandler.expire_access
        elif type_ == "refresh":
            t = JWTHandler.expire_refresh
        else:
            raise ValueError("type must be one of 'access' or 'refresh'")
        expire = datetime.utcnow() + t
        payload.update({"exp": expire})
        return encode(
            payload, JWTHandler.secret_key, algorithm=JWTHandler.algorithm
        )

    @staticmethod
    def decode(token: str) -> dict:
        try:
            return decode(
                token, JWTHandler.secret_key, algorithms=[JWTHandler.algorithm]
            )
        except ExpiredSignatureError as exception:
            raise UnauthorizedException("TokenExpired") from exception
        except InvalidTokenError as exception:
            raise UnauthorizedException("Invalid token") from exception

    @staticmethod
    def decode_expired(token: str) -> dict:
        try:
            return decode(
                token,
                JWTHandler.secret_key,
                algorithms=[JWTHandler.algorithm],
                options={"verify_exp": False},
            )
        except InvalidTokenError as exception:
            raise UnauthorizedException("Invalid token") from exception
