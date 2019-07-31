# from unicodedata import category

from applications.system.schema import Feedback
from common.clients import clients
from common.user_auth import get_user_info, login_user
from model import t_user_feedback, t_user_notice


class SystemService:
    @staticmethod
    def user_sign_in_service(user_id: int):
        user = get_user_info(user_id = user_id)
        return {
            'msg':'success',
            'money':user.monthly
        }

    @staticmethod
    def user_feedback_service( category:str,content:str,contant_no:str):
        with clients.mysql_db.connect() as conn:
            user_id = conn.execute(
                t_user_feedback.insert().values(category=category,
                content=content,contant_no=contant_no)
            )
            token = login_user(user_id=user_id)

            return {'token':token}



    @staticmethod
    def user_share_service():
        pass

    @staticmethod
    def user_invite_service():
        pass

    @staticmethod
    def sys_notice_service(user_id: int):
        with clients.mysql_db.connect() as conn:
          user_notice = conn.execute(t_user_notice.select().where(t_user_notice.c.id == user_id)).fetchone()
        data = {
               'notice_type_id':user_notice.notice_type_id ,
               'full_text_url':user_notice.full_text_url
            }
        return {'data':data}


    @staticmethod
    def switch_notice_service(user_id: int, status: int):
        pass
