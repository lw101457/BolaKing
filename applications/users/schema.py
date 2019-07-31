from typing import Optional

from pydantic import BaseModel


class LoginORegReq(BaseModel):
    mobile: str
    verify_code: str


class TinyLoginReq(BaseModel):
    open_code: str
    open_id: str


class UpdateUserInfoReq(BaseModel):
    category: str
    old_value: str
    new_value: str
