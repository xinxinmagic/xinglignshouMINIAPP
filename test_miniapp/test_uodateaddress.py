# ----------------------- #
#    author:zhangxin      #
#      time:20210104      #
# ----------------------- #
import pytest,time,random
import allure
from MINIapp import updateaddress
from common import logger
from config import env,readConfig,dbconf

upaddre = updateaddress.Updateaddress(env.QA)
db = dbconf.DataLoader(env.QA)
upaddre.header.user_id = readConfig.user_id
upaddre.header.user_token = readConfig.user_token
log = logger.Log()

sql = "SELECT id FROM syds_user.public.user_express_address where user_id = %s"%readConfig.user_id
db.sql_connect("user",sql)
addressid=db.cur.fetchone()[0]
ntime = timenow = time.strftime("%Y%m%d%H%M%S",time.localtime())
phone= random.choice(["13","14","15","17","18"])+"".join(str(random.randint(000000000,999999999)))

case_list = [
    ( addressid,ntime,110100,"北京市",110101,"东城区",ntime+"名",phone,110000,"北京市","","",False,True),

]


@allure.feature('用户修改收货地址')
@allure.description('用户修改收货地址')
@allure.story('用户修改收货地址')
@allure.title('用户修改收货地址')
@pytest.mark.parametrize("addressid,addressDetail,cityCode,cityName,districtCode,districtName,nickName,phone,provinceCode,provinceName,streetCode,streetName,wxImport,err", case_list)
def test_updateaddress(addressid,addressDetail,cityCode,cityName,districtCode,districtName,nickName,phone,provinceCode,provinceName,streetCode,streetName,wxImport,err):
    if addressid:
        res = upaddre.updateaddress(addressid,addressDetail, cityCode, cityName, districtCode, districtName, nickName, phone,
                               provinceCode, provinceName, streetCode, streetName, wxImport)
        log.debug("返回结果：" + str(res))
        assert res['success'] == err

    else:
        log.info("暂无收货地址")



