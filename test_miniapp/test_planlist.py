# ----------------------- #
#    author:zhangxin      #
#      time:20201102      #
# ----------------------- #
import pytest
import allure
from MINIapp import planlivelist
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

pl=planlivelist.planList(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
pl.header.user_id = readConfig.user_id
pl.header.user_token = readConfig.user_token

case_list = [
    (0, 20, True)]


@allure.feature('C端用户预告计划列表')
@allure.description('C端用户预告计划列表')
@allure.story('C端用户预告计划列表')
@allure.title('C端用户预告计划列表')


@pytest.mark.parametrize("offset,pageSize,err",case_list)
def test_planlist (offset,pageSize,err):
    res_1= pl.planlist(offset,pageSize)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


