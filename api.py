import  json, logging, inspect, functools


class APIError(Exception):
    # The base APIError which contains error/data/message
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


# Specific error types
class APIValueError(APIError):

    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value: invalid', field, message)


class APIPermissionError(APIError):

    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission: forbidden', 'permission', message)



class API404Error(APIError):

    def __init__(self, field, message):
        super(API404Error, self).__init__('resource: not found', field, message)