# ----------------------- #
# author:zhangxin         #
# time:202010104          #
# ----------------------- #
import requests
import json
from config import headerconfig, env,readConfig,dbconf
# from common.logger import Log
from common import logger,encryption



class commodityInfo:
    def __init__(self, env):
        self.env = env
        self.log = logger.Log()
        self.header = headerconfig.Platform(env)

    def roomcommodityinfo(self,roomId,commodityCode):
        """
        C端用户直播间商品详情页面

        :param roomId:
        :param shopId:
        :param commodityCode:
        :return:
        """
        url = '%s/webapi/commonModule/commodity/info' % self.env.http_base_url
        params = {
            "roomId":encryption.id_encry(roomId),
            "commodityCode":commodityCode
        }

        content_type = "application/x-www-form-urlencoded"
        # content_type = "application/json"
        headers = self.header.http_header(params,content_type)
        self.log.debug(headers)
        res = requests.get(url=url, params=params, headers=headers).content
        res_json = json.loads(res)
        self.log.debug(res_json)
        return res_json


    def shopcommodityinfo(self,shopId,commodityCode):
        """
        C端用户首页商品详情页面

        :param roomId:
        :param shopId:
        :param commodityCode:
        :return:
        """
        url = '%s/webapi/commonModule/commodity/info' % self.env.http_base_url
        params = {
            "shopId":encryption.id_encry(shopId),
            "commodityCode":commodityCode
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
    ev = env.QA
    pass




