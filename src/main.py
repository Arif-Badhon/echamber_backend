from fastapi.exceptions import RequestValidationError, ValidationError
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
import uvicorn
import os
from fastapi import FastAPI, Request, status
from api.v1.routes import api_router
from db import settings
from exceptions import AppExceptionCase, AppException, app_exception_handler, generic_exception_handler
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI(title='E-Chamber')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(AppExceptionCase)
def custom_app_exception_handler(request: Request, exc: AppException):
    print(exc)
    return app_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            {
                "detail": exc.errors(),
                "body": exc.body,
                "your_additional_errors": {
                    "Will be": "Inside",
                    "This": " Error message",
                },
            }
        ),
    )


@app.exception_handler(ValidationError)
def validation_exception_handler(request: Request, exc: ValidationError):
    print(exc)
    return app_exception_handler(request, AppException.BadRequest(exc))


@app.exception_handler(Exception)
def custom_generic_exception_handler(request: Request, exc: Exception):
    print(exc)
    return generic_exception_handler(request, exc)


# parent path for static file
parent_path = os.path.dirname(os.path.realpath(__file__))


@app.get('/')
def root():
    return {'msg': 'Hello E-Chamber'}


app.mount('/files/', StaticFiles(directory=f'{parent_path}/assets/img'), name='img')


app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1",
                port=8000, reload=True, log_level="info")
