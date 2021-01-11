# ----------------------- #
#    author:zhangxin      #
#      time:20210106      #
# ----------------------- #
import pytest
import allure
from MINIapp import customerinfo
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

info=customerinfo.customerinfo(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
info.header.user_id = readConfig.user_id
info.header.user_token = readConfig.user_token


case_list = [
    (True)

]



@allure.feature('用户信息')
@allure.description('用户信息')
@allure.story('用户信息')
@allure.title('用户信息')
@pytest.mark.parametrize("err",case_list)
def test_customerinfo(err):
    res_1= info.customerinfo()
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


