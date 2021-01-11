# ----------------------- #
#    author:zhangxin      #
#      time:20210105      #
# ----------------------- #
import pytest
import allure
from MINIapp import customer_getlist
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

getlist=customer_getlist.customergetList(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
getlist.header.user_id = readConfig.user_id
getlist.header.user_token = readConfig.user_token

case_list = [
    (0, 20, True)]


@allure.feature('我逛过列表数据')
@allure.description('我逛过列表数据')
@allure.story('我逛过列表数据')
@allure.title('我逛过列表数据')
@pytest.mark.parametrize("offset,pageSize,err",case_list)
def test_getaddresslist (offset,pageSize,err):
    res_1= getlist.customergetList(offset,pageSize)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


