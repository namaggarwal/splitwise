import json
import sys
import os
import pprint

print(__name__)
print(__file__)


class SplitwiseBaseException(Exception):
    """Base exception class for splitwise.

    Attributes:
        message(str, optional): Exception message
        http_body(str, optional): HTTP body
        http_status(int, optional): HTTP status code
        http_headers(:obj:`dict`, optional): Dict containing header key and value
        errors(:obj:`json`, optional): JSON errors
    """

    def __init__(
        self,
        message=None,
        http_body=None,
        http_status=None,
        http_headers=None,
        request=None,
    ):
        """
        Args:
              message(str, optional): Exception message
              http_body(str, optional): HTTP body
              http_status(int, optional): HTTP status code
              http_headers(:obj:`dict`, optional): Dict containing header key and value
        """
        super(SplitwiseBaseException, self).__init__(message)

        if http_body and hasattr(http_body, "decode"):
            try:
                http_body = http_body.decode("utf-8")
            except BaseException:
                http_body = "<Could not decode body as utf-8>"

        self._message = message
        self.http_body = http_body
        self.http_status = http_status
        self.http_headers = http_headers or {}
        self.errors = {}
        self.request = request
        if self.http_body:
            try:
                body = json.loads(self.http_body)
                if "error" in body:
                    self.errors = {"base": body["error"]}
                if "errors" in body:
                    self.errors = body["errors"]
            except Exception:
                pass

    def __str__(self):
        debug = (
            os.environ.get("FLASK_ENV") == "development"
            or "DEBUG" in os.environ
            or "--debug" in sys.argv
        )
        if debug:
            request_lines = [
                f"{self.request.method} {self.request.url}",
                *[": ".join(item) for item in self.request.headers.items()],
                self.request.body,
            ]
            info = {
                "message": self._message,
                "body": self.http_body,
                "status": self.http_headers,
                "errors": self.errors,
                "request": "\n".join(request_lines),
            }
            msg = pprint.pformat(info)
            assert isinstance(msg, str)
            if msg.startswith("<unprintable"):
                msg = repr(info)
            return msg
        msg = self._message or "<empty message>"
        return msg

    def __repr__(self):
        return "%s(message=%r, http_status=%r)" % (
            self.__class__.__name__,
            self._message,
            self.http_status,
        )

    def setMessage(self, message):
        """Sets the exception message
        Args:
              message(str): Exception message
        """
        self._message = message


class SplitwiseException(SplitwiseBaseException):
    """Exception based on requests library Response.

    Inherits: :class:`splitwise.exception.SplitwiseBaseException`
    """

    def __init__(self, message, response=None, request=None):
        """Exception based on requests library Response.

        Args:
            message(str): Exception message
            response(:obj:`requests.Response`, optional): response object from requests library
            request(optional): the request object to render in a debug message
        """
        super(SplitwiseException, self).__init__(
            message=message, request=request
        )

        if response is not None:
            self.http_body = (response.content,)
            self.http_status = (response.status_code,)
            self.http_headers = response.headers


class SplitwiseUnauthorizedException(SplitwiseException):
    """Exception when request to splitwise is unauthorized

    Inherits: :class:`splitwise.exception.SplitwiseException`
    """

    pass


class SplitwiseBadRequestException(SplitwiseException):
    """Exception when request returns bad request

    Inherits: :class:`splitwise.exception.SplitwiseException`
    """

    pass


class SplitwiseNotAllowedException(SplitwiseException):
    """Exception when request to splitwise is not allowed

    Inherits: :class:`splitwise.exception.SplitwiseException`
    """

    pass


class SplitwiseNotFoundException(SplitwiseException):
    """Exception when request to splitwise returns not found

    Inherits: :class:`splitwise.exception.SplitwiseBaseException`
    """

    pass
