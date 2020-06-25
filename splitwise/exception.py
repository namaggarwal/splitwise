class SplitwiseException(Exception):
    def __init__(
        self,
        message=None,
        http_body=None,
        http_status=None,
        http_headers=None
    ):
        super(SplitwiseException, self).__init__(message)

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
        if hasattr(self.http_body, "error"):
            self.errors = {"base": self.http_body["error"]}

        if hasattr(self.http_body, "errors"):
            self.errors = self.http_body["errors"]

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


class SplitwiseUnauthorizedException(SplitwiseException):
    def __init__(
        self,
        message,
        response
    ):

        super(SplitwiseUnauthorizedException, self).__init__(
          message=message,
          http_body=response.content,
          http_status=response.status_code,
          http_headers=response.headers
        )


class SplitwiseBadRequestException(SplitwiseException):
    pass


class SplitwiseNotFoundException(SplitwiseException):
    def __init__(self, name, id, response):
        super(SplitwiseNotFoundException, self).__init__(
            "%s(%r with id %r does not exist)" % (self.__class__.__name__, name, id),
            http_body=response.content,
            http_status=404,
            http_headers=response.headers
        )
