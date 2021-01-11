# ----------------------- #
# author:zhangxin         #
# time:202010106          #
# ----------------------- #
import requests
import json
from config import headerconfig, env,readConfig,dbconf
# from common.logger import Log
from common import logger,encryption



class ordertraces:
    def __init__(self, env):
        self.env = env
        self.log = logger.Log()
        self.header = headerconfig.Platform(env)

    def ordertraces(self,orderCode):
        """
        订单物流

        :param orderCode：
        :return:
        """
        url = '%s/webapi/customer/order/traces'%self.env.http_base_url
        params = {
            "orderCode":orderCode,
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





