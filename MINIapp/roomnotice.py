# ----------------------- #
# author:zhangxin         #
# time:20201109           #
# ----------------------- #
import requests
import json
from config import headerconfig, env
# from common.logger import Log
from common import logger,encryption



class Roomnotice:
    def __init__(self, env):
        self.env = env
        self.log = logger.Log()
        self.header = headerconfig.Platform(env)


    def roomnotice(self,roomId):
        """
        直播预告

        :param roomId:
        :return:
        """
        url = '%s/webapi/liveroom/customer/room/notice' % self.env.http_base_url
        params = {
            "roomId":encryption.id_encry(roomId)
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
    l = Roomnotice(env.QA)
    res = l.roomnotice(1)
    print(type(res))
