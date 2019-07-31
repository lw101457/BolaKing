from fastapi import Depends

from applications.system.schema import Feedback
from common.user_auth import SessionUser
from common.user_auth import current_user
from .router import router
from .service import SystemService


@router.get("/sign-in")
def user_sign_in_api(user: SessionUser = Depends(current_user)):
    """用户签到"""
    return SystemService.user_sign_in_service(user_id=user.user_id)


@router.post("/feedback")
def user_feedback_api(category:str,content:str,contant_no:str):
    return SystemService.user_feedback_service( category=category,
                content=content,contant_no=contant_no)


@router.get("/share")
def user_share_api():
    return SystemService.user_share_service()


@router.get("/invite")
def user_invite_api(user:SessionUser = Depends(current_user())):
    return SystemService.user_invite_service( )


@router.get("/notice")
def sys_notice_api(user: SessionUser = Depends(current_user)):
    return SystemService.sys_notice_service(user_id = user.user_id)


@router.get("/switch-notice")
def switch_notice_api(status: int, user: SessionUser = Depends(current_user)):
    return SystemService.switch_notice_service(user_id=user.user_id, status=status)
