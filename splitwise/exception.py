import json


class SplitwiseBaseException(Exception):
    def __init__(
        self,
        message=None,
        http_body=None,
        http_status=None,
        http_headers=None
    ):
        super(SplitwiseBaseException, self).__init__(message)

        if http_body and hasattr(http_body, "decode"):
            try:
                http_body = http_body.decode("utf-8")
            except BaseException:
                http_body = (
                    "<Could not decode body as utf-8>"
                )

        self._message = message
        self.http_body = http_body
        self.http_status = http_status
        self.http_headers = http_headers or {}
        self.errors = {}
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
        msg = self._message or "<empty message>"
        return msg

    def __repr__(self):
        return "%s(message=%r, http_status=%r)" % (
            self.__class__.__name__,
            self._message,
            self.http_status
        )

    def setMessage(self, message):
        self._message = message


class SplitwiseException(SplitwiseBaseException):
    def __init__(
        self,
        message,
        response
    ):

        super(SplitwiseException, self).__init__(
            message=message,
            http_body=response.content,
            http_status=response.status_code,
            http_headers=response.headers
        )


class SplitwiseUnauthorizedException(SplitwiseException):
    pass


class SplitwiseBadRequestException(SplitwiseException):
    pass


class SplitwiseNotAllowedException(SplitwiseException):
    pass


class SplitwiseNotFoundException(SplitwiseException):
    pass
