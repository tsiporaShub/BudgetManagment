from fastapi import Request
import functools
import logging

logging.basicConfig(filename='utils/server.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def log_request(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        request: Request = kwargs['request']
        method = request.method
        path = request.url.path
        logging.info(f"{request.client.host}: {method} {path}")
        response = await func(*args, **kwargs)
        return response

    return wrapper
