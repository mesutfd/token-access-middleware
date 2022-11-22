import os
from functools import wraps
# from starlette.responses import JSONResponse
# from dotenv import load_dotenv

# load_dotenv()
# PRIMARY_TOKEN = os.getenv('PRIMARY_TOKEN')
# EMERGENCY_TOKEN = os.getenv('EMERGENCY_TOKEN')

TOKENS = ['PRIMARY_TOKEN', 'EMERGENCY_TOKEN']


def token_middleware(token):
    def inner_wrapper(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if token in TOKENS:
                return func(*args, **kwargs)
            else:
                raise ValueError('INVALID_TOKEN')

        return decorated_function

    return inner_wrapper
