from fastapi import Depends, UploadFile, File

from common.user_auth import SessionUser, current_user
from .router import router

from .service import UserService
from .schema import LoginORegReq, TinyLoginReq, UpdateUserInfoReq


@router.post("/login")
def login_reg_api(body: LoginORegReq):
    return UserService.login_reg_service(body)


@router.post("/invite-code")
def add_invite_code_api(invite_code: str, user: SessionUser = Depends(current_user)):
    return UserService.add_invite_code_service(user_id=user.user_id, invite_code=invite_code)


@router.post("/tiny-login")
def tiny_login_api(body: TinyLoginReq):
    return UserService.tiny_login_service(body=body)


@router.get("/announce-count")
def get_announce_count_api(user: SessionUser = Depends(current_user)):
    return UserService.get_announce_count_service(user_id=user.user_id)


@router.get("/user-info")
def get_user_info_api(user: SessionUser = Depends(current_user)):
    return UserService.get_user_info_service(user_id=user.user_id)


@router.post("/user-info")
def update_user_info_api(body: UpdateUserInfoReq, user: SessionUser = Depends(current_user)):
    return UserService.update_user_info_service(body=body, user_id=user.user_id)


@router.post("/head_image")
def update_head_image_api(file: UploadFile = File(...), user: SessionUser = Depends(current_user)):
    return UserService.update_head_image(file=file, user_id=user.user_id)


@router.get("/logout")
def logout_api(user: SessionUser = Depends(current_user)):
    UserService.logout_service(user_id=user.user_id)
