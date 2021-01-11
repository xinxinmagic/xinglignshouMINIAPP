# ----------------------- #
#    author:zhangxin      #
#      time:20210104      #
# ----------------------- #
import pytest
import allure
from MINIapp import commodityinfo
from common import logger
from config import env,dbconf,readConfig

ev=env.QA
ci=commodityinfo.commodityInfo(ev)
db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
ci.header.user_id = readConfig.user_id
ci.header.user_token = readConfig.user_token

sql = "SELECT room_id,item_code FROM syds_common.public.live_room_item WHERE item_status =0 ORDER BY room_id DESC"
db.sql_connect("common", sql)
roomid = db.cur.fetchone()[0]
commodityCode = db.cur.fetchone()[1]

case_list = [
    (roomid, commodityCode, True)]


@allure.feature('C端用户直播间商品详情页面')
@allure.description('C端用户直播间商品详情页面')
@allure.story('C端用户直播间商品详情页面')
@allure.title('C端用户直播间商品详情页面')
@pytest.mark.parametrize("roomId,commodityCode,err",case_list)
def test_roomcommodityinfo(roomId,commodityCode,err):
    res_1= ci.roomcommodityinfo(roomId,commodityCode)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err



sql = "SELECT shop_id,code FROM syds_item.public.item_commodity WHERE status =1"
db.sql_connect("item", sql)
shopid = db.cur.fetchone()[0]
commodityCode1 = db.cur.fetchone()[1]
case_list1 = [
    (shopid,commodityCode1,True)
]
@allure.feature('C端用户首页商品详情页面')
@allure.description('C端用户首页商品详情页面')
@allure.story('C端用户首页商品详情页面')
@allure.title('C端用户首页商品详情页面')
@pytest.mark.parametrize("shopId,commodityCode1,err",case_list1)
def test_shopcommodityinfo(shopId,commodityCode1,err):
    res_1= ci.shopcommodityinfo(shopId,commodityCode1)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


