class BaseException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class ParseError(BaseException):
    def __init__(self, message):
        super().__init__(message)