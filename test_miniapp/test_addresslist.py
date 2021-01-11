# ----------------------- #
#    author:zhangxin      #
#      time:20210104      #
# ----------------------- #
import pytest
import allure
from MINIapp import getaddresslist
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

getlist=getaddresslist.addressList(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
getlist.header.user_id = readConfig.user_id
getlist.header.user_token = readConfig.user_token

case_list = [
    (1, 20, True)]


@allure.feature('查询用户收货地址列表')
@allure.description('查询用户收货地址列表')
@allure.story('查询用户收货地址列表')
@allure.title('查询用户收货地址列表')
@pytest.mark.parametrize("page,pageSize,err",case_list)
def test_getaddresslist (page,pageSize,err):
    res_1= getlist.addresslist(page,pageSize)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


