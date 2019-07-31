"""
    用户认证中心:
        1. login
        2. logout
"""
import string
from datetime import datetime

import ujson as json
from fastapi import Security
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, ValidationError
from sqlalchemy import select

from common.clients import clients
from common.errors import raise_401
from common.global_utils import id_generator
from model import t_user_info

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")
VALID_KEY_CHARS = string.ascii_lowercase + string.digits
TOKEN_REDIS_EXPIRES = 60 * 60 * 24


class SessionUser(BaseModel):
    nickname: str
    user_id: int
    quiz_total: int
    invite_total: int
    head_image: str
    quiz_win_total: int
    daily: int
    weekly: int
    monthly: int


def login_user(user_id, base_record=None):
    """后台用户登录"""
    token = str(id_generator(datetime.now()))  # 随机生成64位分布式唯一机器码
    # 将token和用户信息都存入redis,用于登录和安全校验
    if not base_record:
        sql = '''
        select 
        ui.nickname,ui.quiz_total,ui.invite_total,ui.head_image,ui.quiz_win_total
        ,uac.daily,uac.monthly,uac.weekly
        from
        user_info as ui inner join user_announce_count as uac on ui.id = uac.user_id 
        where ui.id = {}
        '''.format(user_id)
        with clients.mysql_db.connect() as conn:
            base_record = conn.execute(sql).fetchone()
    user_info = SessionUser(
        user_id=user_id,
        nickname=base_record.nickname,
        quiz_total=base_record.quiz_total,
        invite_total=base_record.invite_total,
        head_image=base_record.head_image,
        quiz_win_total=base_record.quiz_win_total,
        daily=base_record.daily,
        weekly=base_record.weekly,
        monthly=base_record.monthly,
    )

    pl = clients.session_redis.pipeline()
    pl.setex(
        '{}'.format(token),
        TOKEN_REDIS_EXPIRES,
        user_info.json()
    )
    pl.setex(
        'token_{}'.format(user_id),
        TOKEN_REDIS_EXPIRES,
        token
    )
    pl.execute()
    return token


def logout_user(user_id):
    redis = clients.session_redis
    token = redis.get('token_{}'.format(user_id))
    if token:
        redis.delete('token_{}'.format(user_id))
        redis.delete('{}'.format(token.decode()))


def get_user_info(user_id):
    redis = clients.session_redis
    token = redis.get('token_{}'.format(user_id)).decode()
    return current_user(token=token)


def current_user(token: str = Security(oauth2_scheme)):
    """获取当前用户数据"""
    # token过期
    user = clients.session_redis.get(token)
    if not user:
        raise_401("登录过期")
    # 用户不存在
    try:
        user = SessionUser(**json.loads(user.decode()))
    except ValidationError:
        raise_401("用户不存在")

    return user


def update_user_cache(user_id, **kwargs):
    """更新用户redis缓存数据: token对应的redis key-value信息更新等"""

    redis = clients.session_redis
    token = redis.get('token_{}'.format(user_id))
    if token:
        user = redis.get(token.decode())
        if user:
            user = SessionUser(**json.loads(user.decode()))
            # 需要严格保证时效的时候使用ttl
            ttl = redis.ttl(token.decode())
            for k, v in kwargs.items():
                setattr(user, k, v)
            redis.setex(
                token.decode(), ttl,
                user.json())


def update_user_cache_better(user_id, **kwargs):
    """优化版user update"""
    redis = clients.session_redis
    token = redis.get("token_{}".format(user_id))
    if token:
        user = redis.get(token.decode())
        if user:
            user = json.loads(user.decode("utf-8"))
            # 需要严格保证时效的时候使用ttl
            ttl = redis.ttl(token.decode())
            user.update(dict(kwargs))
            redis.setex(
                token.decode(), ttl,
                user.json())
