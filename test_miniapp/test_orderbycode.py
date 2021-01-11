# ----------------------- #
#    author:zhangxin      #
#      time:20210106      #
# ----------------------- #
import pytest
import allure
from MINIapp import order_bycode
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

bycode=order_bycode.orderbycode(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
bycode.header.user_id = readConfig.user_id
bycode.header.user_token = readConfig.user_token

sql ="SELECT order_code FROM syds_trade.public.trade_shop_order WHERE buyer_id=52 AND buyer_delete_time=0 ORDER BY id DESC "
db.sql_connect("trade",sql)
orderCode = db.cur.fetchone()[0]
case_list = [
    (orderCode,True)

]

@allure.feature('订单详情')
@allure.description('订单详情')
@allure.story('订单详情')
@allure.title('订单详情')
@pytest.mark.parametrize("orderCode,err",case_list)
def test_orderbycode(orderCode,err):
    res_1= bycode.orderbycode(orderCode)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


