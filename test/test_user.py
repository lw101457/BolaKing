from . import CommonTestCase
from applications.users.service import UserService
from applications.users.schema import *


class UserTestCase(CommonTestCase):
    def test_user_login(self):
        param = {
            "mobile": "13421843857",
            "verify_code": "8888"
        }
        body = LoginORegReq(**param)
        result = UserService.login_reg_service(body)
        print(result)
        assert isinstance(result, dict)
