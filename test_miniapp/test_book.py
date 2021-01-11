# ----------------------- #
#    author:zhangxin      #
#      time:20201109      #
# ----------------------- #
import pytest
import allure
from MINIapp import booked
from common import logger
from config import env,readConfig,dbconf

bo = booked.Book(env.QA)
db = dbconf.DataLoader(env.QA)
bo.header.user_id = readConfig.user_id
bo.header.user_token = readConfig.user_token
log = logger.Log()
# 获取roomid
sql = "SELECT id FROM syds_common.public.live_room WHERE status in(0,1) "
db.sql_connect("common",sql)
roomid = db.cur.fetchone()
print(roomid)
case_list = [
    ( roomid,True),

]


@allure.feature('用户订阅直播')
@allure.description('用户订阅直播')
@allure.story('用户订阅直播')
@allure.title('用户订阅直播')
@pytest.mark.parametrize("roomId,err", case_list)
def test_roomnotice(roomId,err):
    if roomid:
        res = bo.book(roomId[0])
        log.debug("返回结果：" + str(res))
        assert res['success'] == err

    else:
        log.debug("需要新建直播预告")


