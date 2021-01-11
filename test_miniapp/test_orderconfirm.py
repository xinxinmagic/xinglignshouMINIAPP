# ----------------------- #
#    author:zhangxin      #
#      time:20210106      #
# ----------------------- #
import pytest
import allure
from MINIapp import order_confirm
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

confirm=order_confirm.orderconfirm(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
confirm.header.user_id = readConfig.user_id
confirm.header.user_token = readConfig.user_token

sql ="SELECT order_code FROM syds_trade.public.trade_shop_order WHERE buyer_id=52 and order_status='PROD_SENDED' ORDER BY id DESC"
db.sql_connect("trade",sql)
orderCode = db.cur.fetchone()[0]
case_list = [
    (orderCode,True)

]



@allure.feature('订单确认收货')
@allure.description('订单确认收货')
@allure.story('订单确认收货')
@allure.title('订单确认收货')
@pytest.mark.parametrize("orderCode,err",case_list)
def test_orderconfirm(orderCode,err):
    res_1= confirm.orderconfirm(orderCode)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


