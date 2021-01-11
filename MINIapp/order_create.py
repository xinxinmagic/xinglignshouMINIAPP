# ----------------------- #
# author:zhangxin         #
# time:202010105          #
# ----------------------- #
import requests
import json
from config import headerconfig, env,readConfig,dbconf
# from common.logger import Log
from common import logger,encryption



class order_create:
    def __init__(self, env):
        self.env = env
        self.log = logger.Log()
        self.header = headerconfig.Platform(env)

    def order_create(self,buyerAddressId,payType,priceTotal,shopId,remark,skuId,num,price,hideRoomId,guideCode,freightAmount):
        """
        下订单

        :param buyerId:  "string,买家id"
        :param buyerAddressId: string,买家收货地址
        :param payType: 订单类型,为空则为默认的普通订单
        :param isPayReceive: string,是否货到付款
        :param channelId: string,渠道
        :param priceTotal
        :param shopId: string,店铺id
        :param remark: string,备注
        :param splitProportion: string,平台分账比例
        :param skuId: string,购买规格
        :param num:购买数量
        :param price: 价格
        :param hideRoomId: string,直播间id，可以为空
        :param guideCode: string,导购code，可以为空
        :param freightAmount: string,邮费
        :return:
        """
        url = '%s/webapi/customer/order/create' % self.env.http_base_url
        params = {
            "buyerId": readConfig.user_id,
            "buyerAddressId": buyerAddressId,
            "payType":payType,
            "isPayReceive": "1",
            "channelId": 1,
            "priceTotal" : priceTotal,
            "shopOrderRequestList": [
                {
                    "shopId": shopId,
                    "remark": remark,
                    "itemOrderRequestList": [
                        {
                            "skuId": skuId,
                            "num": num,
                            "price":price,
                        }
                    ]
                }
            ],
            "hideRoomId": hideRoomId,
            "guideCode":guideCode,
            "freightAmount": freightAmount
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
    ev = env.QA
    db = dbconf.DataLoader(ev)
    sql = "SELECT room_id,item_code FROM syds_common.public.live_room_item WHERE item_status =0 "
    db.sql_connect("common", sql)
    roomid = db.cur.fetchone()
    print(roomid)




