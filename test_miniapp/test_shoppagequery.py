# ----------------------- #
#    author:zhangxin      #
#      time:20210105      #
# ----------------------- #
import pytest
import allure
from MINIapp import shop_pagequery
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

shp=shop_pagequery.shoppagequery(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
shp.header.user_id = readConfig.user_id
shp.header.user_token = readConfig.user_token

sql ="SELECT id FROM syds_shop.public.sp_shop ORDER BY id DESC"
db.sql_connect("shop",sql)
shopid =db.cur.fetchone()[0]
case_list = [
    (shopid, True)]


@allure.feature('店铺主页')
@allure.description('店铺主页')
@allure.story('店铺主页')
@allure.title('店铺主页')
@pytest.mark.parametrize("shopid,err",case_list)
def test_shoppagequery(shopid,err):
    res_1= shp.shoppagequery(shopid)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


