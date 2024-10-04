""" FastAPI Boilerplate Library """
import requests
import uvicorn
from fastapi import FastAPI

from src.core.logger import logger
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    """Logging middleware"""

    async def dispatch(self, request, call_next):
        logger.info('Logging middleware')
        logger.info(f'Request: {request.method} {request.url}')
        response = await call_next(request)
        logger.info(f'Response: {response.status_code}')
        return response


app = FastAPI(
    debug=False,
)
app.add_middleware(LoggingMiddleware)


def _hello() -> dict:
    """Hello world"""
    logger.info('Hello World')
    return {'message': 'Hello World'}


def _request() -> str:
    """Request example"""
    response = requests.get('https://google.com')
    result = f'Google Response: {response.status_code}'
    logger.info(result)
    return result


def _raise_error() -> str:
    """Raise Error"""
    e: Exception = Exception('This is an exception message')
    try:
        a = 1 / 0
    except Exception as e:
        logger.error(e)
        logger.exception('RRRR - Divide by zero error')
        return str(e)
    return str(a)


@app.get('/hello')
async def hello() -> dict:
    """Hello world"""
    return _hello()


@app.get('/request')
async def request() -> str:
    """Request example"""
    return _request()


@app.get('/raise_error')
async def raise_error() -> str:
    """Raise Error"""
    return _raise_error()


if __name__ == '__main__':

    # Test the color handler
    logger.info("API is starting up")

    _hello()
    _request()
    _raise_error()

    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=8000,
        log_config='core/log_conf.yaml',
    )
