
from app.core.config import settings
# from xml.dom import ValidationErr
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from datetime import datetime
from app.models.user_model import User
from app.schemas.auth_schema import TokenPayload
from jose import jwt
from app.services.user_service import UserService
from pydantic import ValidationError
reuseable_oauth=OAuth2PasswordBearer(
  
  tokenUrl=f"{settings.API_V1_STR}/auth/login",
  scheme_name="JWT"
  
)
async def get_current_user(token: str = Depends(reuseable_oauth))-> User:
  try:
    payload=jwt.decode(token,settings.JWT_SECRET_KEY,algorithms=[settings.ALGORITHM])
    
    token_data = TokenPayload(**payload)
    if datetime.fromtimestamp(token_data.exp)<datetime.now():
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token expired",
        headers={"WWW-Authenticate":"Bearer"},
      )
  except(jwt.JWTError,ValidationError):
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="Could not validate credentials",
      headers={"WWW-Authenticate":"Bearer"},
    )
  user =await UserService.get_user_by_id(token_data.sub)
  
  if not user:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="User not found"
    )
  return user
    
    
          

  