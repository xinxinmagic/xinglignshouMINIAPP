# ----------------------- #
#    author:zhangxin      #
#      time:20210106      #
# ----------------------- #
import pytest
import allure
from MINIapp import order_traces
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

traces=order_traces.ordertraces(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
traces.header.user_id = readConfig.user_id
traces.header.user_token = readConfig.user_token

sql ="SELECT order_code FROM syds_trade.public.trade_shop_order WHERE buyer_id=%s and order_status in('PROD_SENDED','CONFIRM_FINISHED','CONFIRM_TIMEOUT_FINISHED') ORDER BY id DESC"%readConfig.user_id
db.sql_connect("trade",sql)
orderCode = db.cur.fetchone()[0]
print(orderCode)
case_list = [
    (orderCode,True)

]



@allure.feature('订单物流')
@allure.description('订单物流')
@allure.story('订单物流')
@allure.title('订单物流')
@pytest.mark.parametrize("orderCode,err",case_list)
def test_ordertraces(orderCode,err):
    print(orderCode)
    res_1= traces.ordertraces(orderCode)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


