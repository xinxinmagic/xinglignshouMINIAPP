# ----------------------- #
#    author:zhangxin      #
#      time:20210105      #
# ----------------------- #
import pytest
import allure
from MINIapp import orderpage,order_cancel
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

page=orderpage.orderpage(ev)


db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
page.header.user_id = readConfig.user_id
page.header.user_token = readConfig.user_token


case_list = [
    ("",0, 20, True),
    ("WAIT_FOR_PAY",0, 20, True),
    ("WAIT_FOR_SEND",0, 20, True),
    ("WAIT_FOR_SECEVICE",0, 20, True),
]


@allure.feature('订单列表')
@allure.description('订单列表')
@allure.story('订单列表')
@allure.title('订单列表')
@pytest.mark.parametrize("orderStatus,offset,pageSize,err",case_list)
def test_orderpage(orderStatus,offset,pageSize,err):
    res_1= page.orderpage(orderStatus,offset,pageSize)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


