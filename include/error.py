import builtins
import sys





def CreateError(error_name, message):
    error_class = getattr(builtins, error_name, Exception)
    raise error_class(message)
