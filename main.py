from services.auth_jwt import jwt_authentication, fastapi_users, SECRET

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from routers import notes, text_ocr, product
from db import database
from schemas.user_schema import UserDB

#Create the tables, not for production
# metadata.create_all(engine)
app = FastAPI()

# Add static files
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# fastapi users logic pre/before auth
def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")


def on_after_forgot_password(user: UserDB, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token: {token}")


# Custom routs
app.include_router(notes.router, prefix='/notes', tags=['notes'])
app.include_router(text_ocr.router, prefix='/image', tags=['ocr'])
app.include_router(product.router, prefix='/product', tags=['product'])

# Fastapi user auth routs
app.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["auth"]
)
app.include_router(
    fastapi_users.get_reset_password_router(
        SECRET, after_forgot_password=on_after_forgot_password
    ),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])
