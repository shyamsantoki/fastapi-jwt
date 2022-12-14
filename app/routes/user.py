from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import CreateUser
from app.utils.schema import get_db

router = APIRouter()


@router.post("/user")
def create_user(request: CreateUser, db: Session = Depends(get_db)):
    user = User(
        username=request.username,
        password=request.password,
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        gender=request.gender,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# def create_user(request:schemas.user.CreateUser, db: Session = Depends(get_db):
#     user = models.user.User(
#         username=request.username,
#         password=request.password

#     )
