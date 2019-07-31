import uuid
from datetime import datetime

import oss2
from fastapi import UploadFile
from sqlalchemy import and_

from applications.users.schema import LoginORegReq, TinyLoginReq, UpdateUserInfoReq
from common.cached.redis_cached import hget_verify_code
from common.clients import clients
from common.constants.user import cate_sql_map
from common.errors import raise_400
from common.global_utils import default_name_gen
from common.oss_upload import upload_image
from common.user_auth import login_user, get_user_info, logout_user
from model import t_user_info, t_user_announce_count


class UserService:

    @staticmethod
    def login_reg_service(body: LoginORegReq):
        """app 登录"""
        mobile = body.mobile
        if body.verify_code != hget_verify_code(mobile):
            raise_400(code=100)  # 验证码错误
        with clients.mysql_db.connect() as conn:
            row = conn.execute(t_user_info.select().where(t_user_info.c.mobile == mobile)).fetchone()
            if row:
                token = login_user(user_id=row.id)
                is_new = 0
            else:
                # 注册
                nickname, invite_code = default_name_gen(datetime.now())
                user_id = conn.execute(
                    t_user_info.insert().values(mobile=mobile, nickname=nickname, invite_code=invite_code)).lastrowid
                conn.execute(t_user_announce_count.insert().values(user_id=user_id))
                token = login_user(user_id=user_id)
                is_new = 1
        return {"token": token, "is_new": is_new}

    @staticmethod
    def tiny_login_service(body: TinyLoginReq):
        """微信登录"""
        with clients.mysql_db.connect() as conn:
            if body.open_code:
                open_id = ""  # get open_id
                nickname, invite_code = default_name_gen(datetime.now())
                user_id = conn.execute(
                    t_user_info.insert().values(open_id=open_id, nickname=nickname, invite_code=invite_code)).lastrowid
                conn.execute(t_user_announce_count.insert().values(user_id=user_id))
                token = login_user(user_id=user_id)
                is_new = 1
            else:
                row = conn.execute(t_user_info.select().where(t_user_info.c.open_id == body.open_id)).fetchone()
                token = login_user(user_id=row.id)
                is_new = 0
            return {"token": token, "is_new": is_new}

    @staticmethod
    def add_invite_code_service(user_id: int, invite_code: str):
        """用户填写邀请码"""
        with clients.mysql_db.connect() as conn:
            rowcount = conn.execute(
                t_user_info.update().values(invite_code=invite_code).where(and_(
                    t_user_info.c.user_id == user_id,
                    t_user_info.c.invite_code == "",
                ))).rowcount
            if rowcount == 0:
                raise_400(102)  # "重复填写邀请码"
            # TODO(谭):实时在当日增加邀请人的金币数额

        return {"msg": "success"}

    @staticmethod
    def get_announce_count_service(user_id: int):
        user = get_user_info(user_id=user_id)
        return {
            "msg": "success",
            "data": {
                "daily": user.daily,
                "weekly": user.weekly,
                "monthly": user.monthly
            }
        }

    @staticmethod
    def get_user_info_service(user_id: int):
        with clients.mysql_db.connect() as conn:
            user_info = conn.execute(t_user_info.select().where(t_user_info.c.id == user_id)).fetchone()
        data = {
            "head_image": user_info.head_image,
            "nickname": user_info.nickname,
            "email": user_info.email,
            "real_name": user_info.real_name,
            "birthday": user_info.birthday,
            "mobile": user_info.mobile,
            "wechat": user_info.wechat,
            "qq": user_info.qq,
            "family_addr": user_info.family_addr
        }
        return {"msg": "success", "data": data}

    @staticmethod
    def update_user_info_service(body: UpdateUserInfoReq, user_id: int):
        update_sql = cate_sql_map.get(body.category, None)
        if update_sql is None:
            raise_400("错误请求")
        update_sql = update_sql.format(body.new_value, user_id)
        if body.old_value:
            update_sql += "and {0} = {1}".format(body.category, body.old_value)
        with clients.mysql_db.connect() as conn:
            conn.execute(update_sql)
        return {"msg": "success"}

    @staticmethod
    def update_mobile(user_id: int, mobile: str, verify_code: str):
        if verify_code != hget_verify_code(mobile):
            raise_400(code=100)  # 验证码错误
        with clients.mysql_db.connect() as conn:
            conn.execute(t_user_info.update().values(mobile=mobile).where(t_user_info.c.id == user_id))
        return {"msg": "success"}

    @staticmethod
    def update_head_image(file: UploadFile, user_id: int):
        """文件上传"""
        image_url = upload_image(file=file)
        with clients.mysql_db.connect() as conn:
            conn.execute(t_user_info.update().values(head_image=image_url).where(t_user_info.c.id == user_id))
        return {"msg": "success"}

    @staticmethod
    def logout_service(user_id: int):
        login_user(user_id=user_id)
        return {"msg": "success"}
