# ----------------------- #
#    author:zhangxin      #
#      time:20210106      #
# ----------------------- #
import pytest
import allure
from MINIapp import customer_updateAvatar,customer_updateGender,customer_updateName
from common import logger
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

ava=customer_updateAvatar.updateAvatar(ev)
gen = customer_updateGender.updateGender(ev)
name = customer_updateName.updateName(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
ava.header.user_id = readConfig.user_id
ava.header.user_token = readConfig.user_token
gen.header.user_id = readConfig.user_id
gen.header.user_token = readConfig.user_token
name.header.user_id = readConfig.user_id
name.header.user_token = readConfig.user_token


case_list = [
    ("https://vipshop-test.oss-cn-shanghai.aliyuncs.com/70d57807-717c-4376-a1b0-8a88c8496187_a7.jpg",True)
]
@allure.feature('更新用户信息头像')
@allure.description('更新用户信息头像')
@allure.story('更新用户信息头像')
@allure.title('更新用户信息头像')
@pytest.mark.parametrize("avatar,err",case_list)
def test_updatecustomeravatar(avatar,err):
    res_1= ava.updateAvatar(avatar)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err



case_list1 = [
    (1,True)
]
@allure.feature('更新用户性别')
@allure.description('更新用户性别')
@allure.story('更新用户性别')
@allure.title('更新用户性别')
@pytest.mark.parametrize("gender,err",case_list1)
def test_updatecustomergender(gender,err):
    res_1= gen.updateGender(gender)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err


case_list2= [
    ("zhangxin",True)
]
@allure.feature('更新用户姓名')
@allure.description('更新用户姓名')
@allure.story('更新用户姓名')
@allure.title('更新用户姓名')
@pytest.mark.parametrize("personName,err",case_list2)
def test_updatecustomername(personName,err):
    res_1= name.updateName(personName)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err