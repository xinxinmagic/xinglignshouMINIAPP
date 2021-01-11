# ----------------------- #
#    author:zhangxin      #
#      time:20210104      #
# ----------------------- #
import pytest
import allure
from MINIapp import address_delete
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

delid=address_delete.addressdelete(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
delid.header.user_id = readConfig.user_id
delid.header.user_token = readConfig.user_token

sql = "SELECT id FROM syds_user.public.user_express_address where user_id = %s"%readConfig.user_id
db.sql_connect("user",sql)
addressid=db.cur.fetchone()[0]
case_list = [
    (addressid, True)]


@allure.feature('用户删除收货地址')
@allure.description('用户删除收货地址')
@allure.story('用户删除收货地址')
@allure.title('用户删除收货地址')
@pytest.mark.parametrize("addressid,err",case_list)
def test_deleteaddress (addressid,err):
    res_1= delid.addressdelete(addressid)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


