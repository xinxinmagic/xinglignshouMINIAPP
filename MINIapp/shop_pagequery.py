# ----------------------- #
# author:zhangxin         #
# time:202010105          #
# ----------------------- #
import requests
import json
from config import headerconfig, env,readConfig,dbconf
# from common.logger import Log
from common import logger,encryption



class shoppagequery:
    def __init__(self, env):
        self.env = env
        self.log = logger.Log()
        self.header = headerconfig.Platform(env)

    def shoppagequery(self,shopId):
        """
        店铺主页
       "section": {
        "LIVE": {
            "show": "bool,是否展示，true：展示，false可以不传" },
        "LIVE_V2": {
            "show": "bool,是否展示，true：展示，false可以不传" },
        "LIVE_PLAN": {
            "show": "bool,是否展示，true：展示，false可以不传"},
        "COMMODITY_TYPE": {
            "show": "bool,是否展示，true：展示，false可以不传"},
        "BASE_INFO": {
            "show": "bool,是否展示，true：展示，false可以不传" },
        "COMMODITY": {
            "offset": "int,偏移量",
            "show": "bool,是否展示，true：展示，false可以不传",
            "needTotalSize": "bool,是否需要总条数，true：要",
            "pageSize": "init,分页展示数量",
            "commodityTypeId": "string,商品分类id，默认不传获取全部" },
        "SHOP_WINDOW": {
            "show": "bool,是否展示，true：展示，false可以不传" }},
        "shopId": "string,店铺id"
        """
        url = '%s/webapi/customer/shop/page/query' % self.env.http_base_url
        params = {
            "section": {
                "LIVE": {
                    "show": True
                },
                "LIVE_V2": {
                    "show": True
                },
                "LIVE_PLAN": {
                    "show": True
                },
                "COMMODITY_TYPE": {
                    "show": True
                },
                "BASE_INFO": {
                    "show": True
                },
                "COMMODITY": {
                    "offset": 0,
                    "show": True,
                    "needTotalSize": True,
                    "pageSize": 20
                },
                "SHOP_WINDOW": {
                    "show": True
                                }
            },
            "shopId": encryption.id_encry(shopId)
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




