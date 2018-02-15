class FormateException(Exception):
    def __init__(self, error='Formate Exception'):
        Exception.__init__(self, error)


class InputFormateInsException(FormateException):
    def __init__(self, error='InputFormate has no instantiateinstantiate'):
        Exception.__init__(self, error)
