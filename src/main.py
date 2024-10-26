""" FastAPI Boilerplate Library """
import os
import sys

import uvicorn
from fastapi import FastAPI

# Add the root directory of your project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.api.v1.routers import router
from src.core.config import file_settings
from src.middleware import LoggingMiddleware

app = FastAPI(
    debug=False,
)
app.add_middleware(LoggingMiddleware)

app.include_router(router)


if __name__ == '__main__':

    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=8000,
        log_config=file_settings.log_config_filename,
        reload=True,
    )
