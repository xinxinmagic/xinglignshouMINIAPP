# ----------------------- #
# author:zhangxin         #
# time:202010105          #
# ----------------------- #
import requests
import json
from config import headerconfig, env,readConfig,dbconf
# from common.logger import Log
from common import logger



class customergetList:
    def __init__(self, env):
        self.env = env
        self.log = logger.Log()
        self.header = headerconfig.Platform(env)

    def customergetList(self,offset,pageSize):
        """
        我逛过列表数据

        :param offset:
        :param pageSize:
        :return:
        """
        url = '%s/webapi/customer/getList' % self.env.http_base_url
        params = {
            "offset":offset,
            "pageSize":pageSize
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




