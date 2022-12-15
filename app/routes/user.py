from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import DisplayUser, LoginUser, SignupUser
from app.utils.password import get_hashed_password, verify_password
from app.utils.schema import HTTPError, get_db
from app.utils.token import (
    JWTBearer,
    create_access_token,
    create_refresh_token,
    decode_access_token,
)

router = APIRouter()


@router.post(
    "/user/signup",
    description="Signing up a new user",
    responses={
        status.HTTP_201_CREATED: {"model": DisplayUser},
        status.HTTP_409_CONFLICT: {"model": HTTPError},
    },
    response_model=DisplayUser,
    status_code=status.HTTP_201_CREATED,
)
def signup_user(request: SignupUser, db: Session = Depends(get_db)):

    if db.query(User.username).filter(User.username == request.username).count():
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Username is taken")

    user = User(
        username=request.username,
        password=get_hashed_password(request.password),
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        gender=request.gender,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.post(
    "/user/login",
    description="Logging in an existing user",
    responses={
        status.HTTP_200_OK: {"model": DisplayUser},
        status.HTTP_400_BAD_REQUEST: {"model": HTTPError},
    },
    status_code=status.HTTP_200_OK,
)
def login_user(request: LoginUser, response: Response, db: Session = Depends(get_db)):
    if not db.query(User.id).filter(User.username == request.username).count():
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, detail="Username does not exist"
        )
    else:
        user_creds = (
            db.query(User.password, User.id)
            .filter(User.username == request.username)
            .first()
        )
        user_id = user_creds.id
        user_password = user_creds.password
        if verify_password(request.password, user_password):
            access_token = create_access_token(user_id)
            refresh_token = create_refresh_token(user_id)
            response.set_cookie(
                key="access_token",
                value=f"{access_token}",
                httponly=True,
                expires=60,
            )
            # response.headers["Authorization"] = f"Bearer {access_token}"
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
            }
        else:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST, detail="Password is incorrect"
            )


@router.get(
    "/user/me",
    description="Display user information",
    responses={
        status.HTTP_200_OK: {"model": DisplayUser},
        status.HTTP_403_FORBIDDEN: {"model": HTTPError},
    },
    dependencies=[Depends(JWTBearer())],
)
def display_user(request: Request, db: Session = Depends(get_db)):
    access_token = request.headers["authorization"][7:]
    payload = decode_access_token(access_token)
    try:
        user_id = payload["sub"]
        user = db.query(User).filter(User.id == user_id).first()
        print(user)
    except KeyError as exception:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED, detail="Access token is expired"
        ) from exception
    return user
