# ----------------------- #
# author:zhangxin         #
# time:202010105          #
# ----------------------- #
import requests
import json
from config import headerconfig, env,readConfig,dbconf
# from common.logger import Log
from common import logger,encryption



class orderconfirmPage:
    def __init__(self, env):
        self.env = env
        self.log = logger.Log()
        self.header = headerconfig.Platform(env)

    def orderconfirmPage(self,skuKey,quantity):
        """
        订单-确认订单页
        :param skuKey:sku库存id
        :param quantity:数量
        :return:
        """
        url = '%s/webapi/customer/order/confirmPage' % self.env.http_base_url
        params = {
            "order":
                [
                    {"skuKey":skuKey,
                     "quantity":quantity
                     }
                ]
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
    ordercon = orderconfirmPage(env.QA)


    db = dbconf.DataLoader(env.QA)
    log = logger.Log()

    # 获取用户id和token
    ordercon.header.user_id = readConfig.user_id
    ordercon.header.user_token = readConfig.user_token
    res_1 = ordercon.orderconfirmPage(6430, 1)
    buyerAddressId = res_1['object']['defaultAddress']['addressId']
    shopId = res_1['object']['orderWebShow'][0]['shopId']
    skuId = res_1['object']['orderWebShow'][0]['orderItemWebShows'][0]['skuKey']
    num = res_1['object']['orderWebShow'][0]['orderItemWebShows'][0]['quantity']
    price = res_1['object']['orderWebShow'][0]['orderItemWebShows'][0]['price']
    freightAmount = res_1['object']['freightAmount']
    print(freightAmount+price)




