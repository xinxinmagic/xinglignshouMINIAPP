# ----------------------- #
# author:zhangxin         #
# time:20201109           #
# ----------------------- #
import requests
import json
from config import headerconfig, env
# from common.logger import Log
from common import logger,encryption



class Book:
    def __init__(self, env):
        self.env = env
        self.log = logger.Log()
        self.header = headerconfig.Platform(env)


    def book(self,roomId):
        """
        用户订阅直播

        :param roomId:
        :return:
        """
        url = '%s/webapi/liveroom/customer/user/booked' % self.env.http_base_url
        params = {
            "roomId":encryption.id_encry(roomId)
        }

        content_type = "application/x-www-form-urlencoded"
        # content_type = "application/json"
        headers = self.header.http_header(params,content_type)
        self.log.debug(headers)
        res = requests.post(url=url, data=params, headers=headers).content
        res_json = json.loads(res)
        self.log.debug(res_json)
        return res_json


if __name__ == "__main__":
    l = Book(env.QA)
    res = l.book(1)
    print(type(res))
