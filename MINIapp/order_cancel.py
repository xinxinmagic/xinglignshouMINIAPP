# ----------------------- #
# author:zhangxin         #
# time:202010105          #
# ----------------------- #
import requests
import json
from config import headerconfig, env,readConfig,dbconf
# from common.logger import Log
from common import logger,encryption



class ordercancel:
    def __init__(self, env):
        self.env = env
        self.log = logger.Log()
        self.header = headerconfig.Platform(env)

    def ordercancel(self,orderCode):
        """
        取消交易

        :param orderCode：
        :return:
        """
        url = '%s/webapi/customer/order/cancel/%s'%(self.env.http_base_url,orderCode)
        params = {
            "orderCode":orderCode,
        }

        # content_type = "application/x-www-form-urlencoded"
        content_type = "application/json"
        headers = self.header.http_header(params,content_type)
        self.log.debug(headers)
        res = requests.post(url=url, data=json.dumps(params), headers=headers).content
        res_json = json.loads(res)
        self.log.debug(res_json)
        return res_json


if __name__ == "__main__":
    pass





