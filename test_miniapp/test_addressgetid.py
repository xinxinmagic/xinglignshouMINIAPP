# ----------------------- #
#    author:zhangxin      #
#      time:20210104      #
# ----------------------- #
import pytest
import allure
from MINIapp import addressgetid
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

getid=addressgetid.addressgetById(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
getid.header.user_id = readConfig.user_id
getid.header.user_token = readConfig.user_token

sql = "SELECT id FROM syds_user.public.user_express_address where user_id = %s"%readConfig.user_id
db.sql_connect("user",sql)
addressid=db.cur.fetchone()[0]
case_list = [
    (addressid, True)]


@allure.feature('获取用户一条收货地址')
@allure.description('获取用户一条收货地址')
@allure.story('获取用户一条收货地址')
@allure.title('获取用户一条收货地址')
@pytest.mark.parametrize("addressid,err",case_list)
def test_addressgetid (addressid,err):
    res_1= getid.addressgetById(addressid)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


