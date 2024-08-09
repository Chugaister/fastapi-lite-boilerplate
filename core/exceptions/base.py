from http import HTTPStatus


class HTTPError(Exception):
    code = HTTPStatus.BAD_GATEWAY
    error_code = HTTPStatus.BAD_GATEWAY
    message = HTTPStatus.BAD_GATEWAY.description

    def __init__(self, message=None):
        if message:
            self.message = message


class BadRequestException(HTTPError):
    code = HTTPStatus.BAD_REQUEST
    error_code = HTTPStatus.BAD_REQUEST
    message = HTTPStatus.BAD_REQUEST.description


class NotFoundException(HTTPError):
    code = HTTPStatus.NOT_FOUND
    error_code = HTTPStatus.NOT_FOUND
    message = HTTPStatus.NOT_FOUND.description


class ForbiddenException(HTTPError):
    code = HTTPStatus.FORBIDDEN
    error_code = HTTPStatus.FORBIDDEN
    message = HTTPStatus.FORBIDDEN.description


class UnauthorizedException(HTTPError):
    code = HTTPStatus.UNAUTHORIZED
    error_code = HTTPStatus.UNAUTHORIZED
    message = HTTPStatus.UNAUTHORIZED.description


class UnprocessableEntity(HTTPError):
    code = HTTPStatus.UNPROCESSABLE_ENTITY
    error_code = HTTPStatus.UNPROCESSABLE_ENTITY
    message = HTTPStatus.UNPROCESSABLE_ENTITY.description


class ConflictException(HTTPError):
    code = HTTPStatus.CONFLICT
    error_code = HTTPStatus.CONFLICT
    message = HTTPStatus.CONFLICT.description


class MethodNotImplementedException(HTTPError):
    code = HTTPStatus.NOT_IMPLEMENTED
    error_code = HTTPStatus.NOT_IMPLEMENTED
    message = HTTPStatus.NOT_IMPLEMENTED.description
