# ----------------------- #
#    author:zhangxin      #
#      time:20210104      #
# ----------------------- #
import pytest
import allure
from MINIapp import login
from common import logger
from config import env,readConfig,dbconf

l = login.Login(env.QA)
db = dbconf.DataLoader(env.QA)
l.header.user_id = readConfig.user_id
l.header.user_token = readConfig.user_token
log = logger.Log()

case_list = [
    ( True),

]


@allure.feature('登录')
@allure.description('登录')
@allure.story('登录')
@allure.title('登录')
@pytest.mark.parametrize("err", case_list)
def test_login(err):
    res = l.login()
    log.debug("返回结果：" + str(res))
    assert res['success'] == err



