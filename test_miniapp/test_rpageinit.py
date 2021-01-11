# ----------------------- #
#    author:zhangxin      #
#      time:20201102      #
# ----------------------- #
import pytest
import allure
from MINIapp import roompageinit
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

pinit=roompageinit.pageInit(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
pinit.header.user_id = readConfig.user_id
pinit.header.user_token = readConfig.user_token

sql = "SELECT id FROM syds_common.public.live_room WHERE status =1 "
db.sql_connect("common", sql)
roomid = db.cur.fetchone()

case_list = [
    (roomid, True)]


@allure.feature('直播间操作-直播间初始化')
@allure.description('直播间操作-直播间初始化')
@allure.story('直播间操作-直播间初始化')
@allure.title('直播间操作-直播间初始化')
# @pytest.mark.skip(reason="直播房间取消(手动取消)，不测")

@pytest.mark.parametrize("roomId,err", case_list)
def test_pageinit (roomId,err):
    if roomid:
        res_1= pinit.pageinit(roomId[0])
        log.debug("返回结果：" + str(res_1))
        assert res_1['success'] == err
    else:
        log.debug("无正在直播的直播间")




