from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, oauth2
from ..utils import verify_password

router = APIRouter(tags=['Aythentication'])


@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    found_user = db.query(models.User).filter(
        models.User.email == user_credentials.username).one_or_none()

    if not found_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="incorrect email or password")

    is_correct_password = verify_password(
        user_credentials.password, found_user.password)

    if not is_correct_password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="incorrect email or password")

    access_token = oauth2.create_access_token(data={"user_id": found_user.id})

    return {"access_token": access_token, "token_type": "bearer"}
