# ----------------------- #
# author:zhangxin         #
# time:202010105          #
# ----------------------- #
import requests
import json
from config import headerconfig, env,readConfig,dbconf
# from common.logger import Log
from common import logger,encryption



class orderpage:
    def __init__(self, env):
        self.env = env
        self.log = logger.Log()
        self.header = headerconfig.Platform(env)

    def orderpage(self,orderStatus,offset,pageSize):
        """
        订单列表
        :param
        :return:
        """
        url = '%s/webapi/customer/order/page'%self.env.http_base_url
        params = {
            "orderStatus":orderStatus,
            "offset":offset,
            "pageSize":pageSize,
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





