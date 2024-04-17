class BaseException(Exception):
    pass


class FactoryNotFound(BaseException):
    pass


class MethodNotFound(BaseException):
    pass


class ModelNotFound(BaseException):
    pass