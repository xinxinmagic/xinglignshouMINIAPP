# ----------------------- #
# author:zhangxin         #
# time:202010105          #
# ----------------------- #
import requests
import json
from config import headerconfig, env,readConfig,dbconf
# from common.logger import Log
from common import logger,encryption



class orderpay:
    def __init__(self, env):
        self.env = env
        self.log = logger.Log()
        self.header = headerconfig.Platform(env)

    def orderpay(self,payOrderId,payType,openId,paymentChannelCode):
        """

        :param payOrderId:"long,需要支付的平台id,如果payType=1的话，就是platformId，如果paytype=2的话就是商铺订单的id",
        :param payType:"string,支付订单类型,1:平台订单，2.商铺订单",
        :param openId: "string,微信小程序支付需要的openId",
        :param paymentChannelCode:"string,支付渠道,100为小程序，200：支付宝客户端",
        :return:
        """
        url = '%s/webapi/customer/order/pay'%self.env.http_base_url
        params = {
            "payOrderId":payOrderId,
            "payType":payType,
            "openId":openId,
            "paymentChannelCode":paymentChannelCode
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





