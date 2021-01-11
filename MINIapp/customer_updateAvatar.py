# ----------------------- #
# author:zhangxin         #
# time:202010106          #
# ----------------------- #
import requests
import json
from config import headerconfig, env,readConfig,dbconf
# from common.logger import Log
from common import logger,encryption



class updateAvatar:
    def __init__(self, env):
        self.env = env
        self.log = logger.Log()
        self.header = headerconfig.Platform(env)

    def updateAvatar(self,avatar):
        """
        更新用户头像

        :param
        :return:
        """
        url = '%s/webapi/customer/updateAvatar'%self.env.http_base_url
        params = {
            "avatar":avatar

        }

        content_type = "application/x-www-form-urlencoded"
        # content_type = "application/json"
        headers = self.header.http_header(params,content_type)
        self.log.debug(headers)
        res = requests.get(url=url, params=params, headers=headers).content
        res_json = json.loads(res)
        self.log.debug(res_json)
        return res_json


if __name__ == "__main__":
    pass





