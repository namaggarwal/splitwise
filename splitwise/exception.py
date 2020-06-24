class SplitwiseException(Exception):
    def __init__(
        self,
        message=None,
        http_body=None,
        http_status=None,
        headers=None
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
        self.headers = headers or {}
        self.errors = {}
        if "error" in self.http_body:
            self.errors = {"base": self.http_body["error"]}

        if "errors" in self.http_body:
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


class SplitwiseBadRequestException(SplitwiseException):
    pass


class SplitwiseNotFoundException(SplitwiseException):
    def __init__(self, name, id, http_body=None, headers=None):
        super(SplitwiseNotFoundException, self).__init__(
            "%s(%r with id %id does not exist)" % (self.__class__.__name__, name, id), http_body, 404, headers
        )
