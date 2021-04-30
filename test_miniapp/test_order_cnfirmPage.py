# ----------------------- #
#    author:wanglixin      #
#      time:20210429      #
# ----------------------- #
import pytest
import allure
from MINIapp import order_confirmPage
from common import logger
from config import env,dbconf,readConfig
import time,datetime
"""
 订单 - 确认订单页
 :param
  skuKey: sku库存id
 :param
  quantity: 数量
"""
ev = env.QA

confirmPage = order_confirmPage.orderconfirmPage(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
confirmPage.header.user_id = readConfig.user_id
confirmPage.header.user_token = readConfig.user_token
case_list = [
    (6430, 1)
]



@allure.feature('订单 - 确认订单页')
@allure.description('订单 - 确认订单页')
@allure.story('订单 - 确认订单页')
@allure.title('订单 - 确认订单页')
@pytest.mark.parametrize("skuKey,quantity",case_list)
def test_orderconfirmPage(skuKey,quantity):
    res_1= confirmPage.orderconfirmPage(skuKey,quantity)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == True
