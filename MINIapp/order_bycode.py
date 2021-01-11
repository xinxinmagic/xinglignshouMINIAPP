# ----------------------- #
# author:zhangxin         #
# time:202010106          #
# ----------------------- #
import requests
import json
from config import headerconfig, env,readConfig,dbconf
# from common.logger import Log
from common import logger,encryption



class orderbycode:
    def __init__(self, env):
        self.env = env
        self.log = logger.Log()
        self.header = headerconfig.Platform(env)

    def orderbycode(self,orderCode):
        """
        订单详情

        :param orderCode：
        :return:
        """
        url = '%s/webapi/customer/order/%s'%(self.env.http_base_url,orderCode)
        params = {

        }

        # content_type = "application/x-www-form-urlencoded"
        content_type = "application/json"
        headers = self.header.http_header(params,content_type)
        self.log.debug(headers)
        res = requests.get(url=url, data=json.dumps(params), headers=headers).content
        res_json = json.loads(res)
        self.log.debug(res_json)
        return res_json


if __name__ == "__main__":
    pass





