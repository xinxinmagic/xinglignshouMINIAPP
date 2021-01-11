# ----------------------- #
#    author:zhangxin      #
#      time:20210106      #
# ----------------------- #
import pytest
import allure
from MINIapp import order_delete
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

delete=order_delete.orderdelete(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
delete.header.user_id = readConfig.user_id
delete.header.user_token = readConfig.user_token

sql ="SELECT order_code FROM syds_trade.public.trade_shop_order WHERE buyer_id=52 and order_status in('MANUAL_CANCELLED','PAY_TIMEOUT_CANCELLED','UNDER_REVIEW_FAILED_CANCELLED','SEND_TIMEOUT_CANCELLED') AND buyer_delete_time=0 ORDER BY id DESC"
db.sql_connect("trade",sql)
orderCode = db.cur.fetchone()[0]
case_list = [
    (orderCode,True)

]



@allure.feature('删除订单')
@allure.description('删除订单')
@allure.story('删除订单')
@allure.title('删除订单')
@pytest.mark.parametrize("orderCode,err",case_list)
def test_orderdelete(orderCode,err):
    res_1= delete.orderdelete(orderCode)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


