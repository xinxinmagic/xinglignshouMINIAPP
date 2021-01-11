# ----------------------- #
#    author:zhangxin      #
#      time:20210105      #
# ----------------------- #
import pytest
import allure
from MINIapp import shop_windowlist
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

winl=shop_windowlist.shopwindowlist(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
winl.header.user_id = readConfig.user_id
winl.header.user_token = readConfig.user_token

sql ="SELECT id,shop_id FROM syds_shop.public.shop_window WHERE delete_tag=0 ORDER BY id DESC"
db.sql_connect("shop",sql)
shopWindowId = db.cur.fetchone()[0]
shopid =db.cur.fetchone()[1]
case_list = [
    (shopWindowId,shopid,0, 20, True)]


@allure.feature('橱窗全部商品')
@allure.description('橱窗全部商品')
@allure.story('橱窗全部商品')
@allure.title('橱窗全部商品')
@pytest.mark.parametrize("shopWindowId,shopId,offset,pageSize,err",case_list)
def test_shopwindowlist(shopWindowId,shopId,offset,pageSize,err):
    res_1= winl.shopwindowlist(shopWindowId,shopId,offset,pageSize)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


