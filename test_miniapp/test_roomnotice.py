# ----------------------- #
#    author:zhangxin      #
#      time:20201109      #
# ----------------------- #
import pytest
import allure
from MINIapp import roomnotice
from common import logger
from config import env,readConfig,dbconf

notice = roomnotice.Roomnotice(env.QA)
db = dbconf.DataLoader(env.QA)
notice.header.user_id = readConfig.user_id
notice.header.user_token = readConfig.user_token
log = logger.Log()
# 获取roomid
sql = "SELECT id FROM syds_common_dev.public.live_room WHERE status in(0,1) "
db.sql_connect("common",sql)
roomid = db.cur.fetchone()
print(roomid)
case_list = [
    ( roomid,True),

]


@allure.feature('直播预告')
@allure.description('直播预告')
@allure.story('直播预告')
@allure.title('直播预告')
@pytest.mark.parametrize("roomId,err", case_list)

def test_roomnotice(roomId,err):
    if roomid:
        res = notice.roomnotice(roomId[0])
        log.debug("返回结果：" + str(res))
        assert res['success'] == err

    else:
        log.debug("需要新建直播预告")


