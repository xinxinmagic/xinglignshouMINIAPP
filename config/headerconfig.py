# ----------------------- #
#    author:zhangxin      #
#                         #
#      time:20200923      #
#                         #
# ----------------------- #
import time
from common import encryption
from config import env
import requests, json


class Platform:
    def __init__(self, env):
        self.user_id = None
        self.user_token = None
        self.env = env

    def http_header(self, param, content_type):
        header = {
            "a": '1',
            "p": '6',
            "c": '0',
            "v": "1.0.0",
            "t": str(int(time.time() * 1000))
        }
        if self.user_id:
            header["loginUserId"] = self.user_id
        if self.user_token:
            header["loginToken"] = self.user_token

        if content_type == "application/json":
            headers = encryption.sign_encry(header, "")
        else:
            headers = encryption.sign_encry(header, param)

        headers["Content-Type"] = content_type

        return headers

    def login_header(self, p, param, contenttype):
        """
        :param p: SUPER_ADMIN(1, "超管后台"),
                  BRAND_ADMIN(2, "品牌商后台"),
                  SHOP_ADMIN_WEB(3, "分店后台web"),
                  SHOP_ADMIN_APP_IOS(4, "分店后台ios"),
                  SHOP_ADMIN_APP_ANDRIOD(5, "分店后台安卓"),
                  CUSTOMER_XCX(6, "客户端小程序"),
        :param param:
        :param contenttype:
        :return:
        """
        url = '%s/webapi/login' % self.env.http_base_url
        if p == 1:
            params = {
                "username": self.env.super_username,
                "password": encryption.generate_psw(self.env.super_password),
                "p": p
            }
        elif p == 2:
            params = {
                "username": self.env.cloud_user,
                "password": encryption.generate_psw(self.env.cloud_password),
                "p": 1
            }
        elif p == 3:
            params = {
                "username": self.env.shop_user,
                "password": encryption.generate_psw(self.env.shop_password),
                "p": 1
            }
        elif p == 10:
            params = {
                "username": self.env.super_username,
                "password": encryption.generate_psw(self.env.super_password),
                "p": p
            }
        else:
            params = {
                "username": self.env.super_username,
                "password": encryption.generate_psw(self.env.super_password),
                "p": 1
            }

        content_type = "application/x-www-form-urlencoded"
        # content_type = "application/json"
        head = self.http_header(params, content_type)
        res = requests.get(url=url, params=params, headers=head).content
        res_json = json.loads(res)
        print(res_json)

        if res_json['success']:
            self.user_token = res_json['object']['token']
            self.user_id = str(res_json['object']['userVo']['id'])

        headers = self.http_header(param, contenttype)
        return headers


if __name__ == "__main__":
    a = Platform(env.QA)
