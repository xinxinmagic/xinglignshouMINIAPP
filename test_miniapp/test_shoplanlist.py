# ----------------------- #
#    author:zhangxin      #
#      time:20210105      #
# ----------------------- #
import pytest
import allure
from MINIapp import shopplanlist
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

plist=shopplanlist.shopplanList(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
plist.header.user_id = readConfig.user_id
plist.header.user_token = readConfig.user_token

sql ="SELECT id FROM syds_shop.public.sp_shop ORDER BY id DESC"
db.sql_connect("shop",sql)
shopid =db.cur.fetchone()[0]
case_list = [
    (0, 20,shopid, True)]


@allure.feature('V1.1.1 直播预告（一个店铺下的直播预告列表）')
@allure.description('V1.1.1 直播预告（一个店铺下的直播预告列表）')
@allure.story('V1.1.1 直播预告（一个店铺下的直播预告列表）')
@allure.title('V1.1.1 直播预告（一个店铺下的直播预告列表）')
@pytest.mark.parametrize("offset,pageSize,shopid,err",case_list)
def test_shopplanList (offset,pageSize,shopid,err):
    res_1= plist.shopplanList(offset,pageSize,shopid)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


