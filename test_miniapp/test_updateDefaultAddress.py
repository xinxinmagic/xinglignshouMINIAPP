# ----------------------- #
#    author:zhangxin      #
#      time:20210105      #
# ----------------------- #
import pytest
import allure
from MINIapp import updateDefaultAddress
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

updef=updateDefaultAddress.updateDefaultAddress(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
updef.header.user_id = readConfig.user_id
updef.header.user_token = readConfig.user_token

sql = "SELECT id FROM syds_user.public.user_express_address where user_id = %s"%readConfig.user_id
db.sql_connect("user",sql)
addressid=db.cur.fetchone()[0]
case_list = [
    (addressid, True)]


@allure.feature('修改用户默认收货地址')
@allure.description('修改用户默认收货地址')
@allure.story('修改用户默认收货地址')
@allure.title('修改用户默认收货地址')
@pytest.mark.parametrize("addressid,err",case_list)
def test_updateDefaultAddress(addressid,err):
    res_1= updef.updateDefaultAddress(addressid)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err
    sql = "SELECT is_default FROM syds_user.public.user_express_address where id = %s" % addressid
    db.sql_connect("user", sql)
    isdefault = db.cur.fetchone()[0]
    assert isdefault==1


