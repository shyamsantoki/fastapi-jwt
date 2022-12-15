from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import DisplayUser, LoginUser, SignupUser
from app.utils.password import get_hashed_password, verify_password
from app.utils.schema import HTTPError, get_db
from app.utils.token import create_access_token, create_refresh_token

router = APIRouter()


@router.post(
    "/user/signup",
    description="Signing up a new user",
    responses={
        status.HTTP_201_CREATED: {"model": DisplayUser},
        status.HTTP_409_CONFLICT: {"model": HTTPError},
    },
    status_code=status.HTTP_201_CREATED,
)
def signup_user(request: SignupUser, db: Session = Depends(get_db)):
    if db.query(User.username).filter(User.username == request.username).count():
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Username is taken")
    print(request.password)
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
def login_user(request: LoginUser, db: Session = Depends(get_db)):
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
            return {
                "access_token": create_access_token(user_id),
                "refresh_token": create_refresh_token(user_id),
            }
        else:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST, detail="Password is incorrect"
            )
