# ----------------------- #
# author:zhangxin         #
# time:20201109           #
# ----------------------- #
import requests
import json
from config import headerconfig, env,readConfig,dbconf
# from common.logger import Log
from common import logger,encryption



class pageInit:
    def __init__(self, env):
        self.env = env
        self.log = logger.Log()
        self.header = headerconfig.Platform(env)

    def pageinit(self,roomId):
        """
        主播进房页面初始化

        :param roomid:
        :return:
        """
        url = '%s/webapi/liveroom/customer/room/pageInit' % self.env.http_base_url
        params = {
            "roomId":encryption.id_encry(roomId)
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
    pinit = pageInit(ev)
    db = dbconf.DataLoader(ev)

    pinit.header.user_id = readConfig.user_id
    pinit.header.user_token = readConfig.user_token

    sql = "SELECT id FROM syds_common_dev.public.live_room WHERE status =1 "
    db.sql_connect("common", sql)
    roomid = db.cur.fetchone()
    pinit.pageinit(roomid[0])





