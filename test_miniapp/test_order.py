# ----------------------- #
#    author:zhangxin      #
#      time:20210105      #
# ----------------------- #
import pytest
import allure
from MINIapp import order_confirmPage,order_create,orderpay,orderpage,order_cancel
from common import logger,encryption
from config import env,dbconf,readConfig
import time,datetime

ev=env.QA

ordercon=order_confirmPage.orderconfirmPage(ev)
create = order_create.order_create(ev)
pay = orderpay.orderpay(ev)
page=orderpage.orderpage(ev)
cancel = order_cancel.ordercancel(ev)

db = dbconf.DataLoader(ev)
log = logger.Log()

# 获取用户id和token
ordercon.header.user_id = readConfig.user_id
ordercon.header.user_token = readConfig.user_token
create.header.user_id = readConfig.user_id
create.header.user_token = readConfig.user_token
pay.header.user_id = readConfig.user_id
pay.header.user_token = readConfig.user_token
page.header.user_id = readConfig.user_id
page.header.user_token = readConfig.user_token
cancel.header.user_id = readConfig.user_id
cancel.header.user_token = readConfig.user_token

sql = "SELECT id FROM syds_item.public.item_shop_commodity_sku_inventory  WHERE available_size>0 and commodity_id IN(SELECT id  FROM syds_item.public.item_commodity WHERE status=1 and deploy_status=1  ORDER BY id DESC)ORDER BY id DESC"
db.sql_connect("item",sql)
skuKey=db.cur.fetchone()[0]
case_list1 = [
    (skuKey,1, True)]


@allure.feature('确认订单页')
@allure.description('确认订单页')
@allure.story('确认订单页')
@allure.title('确认订单页')
@pytest.mark.parametrize("skuKey,quantity,err",case_list1)
def test_orderconfirmPage (skuKey,quantity,err):
    res_1=ordercon.orderconfirmPage(skuKey,quantity)
    log.debug("返回结果：" + str(res_1))
    assert res_1['success'] == err



res_1=ordercon.orderconfirmPage(skuKey,1)
buyerAddressId = encryption.urltoid(res_1['object']['defaultAddress']['addressId'])
shopId= res_1['object']['orderWebShow'][0]['shopId']
skuId =res_1['object']['orderWebShow'][0]['orderItemWebShows'][0]['skuKey']
num= res_1['object']['orderWebShow'][0]['orderItemWebShows'][0]['quantity']
price = res_1['object']['orderWebShow'][0]['orderItemWebShows'][0]['price']
freightAmount = res_1['object']['freightAmount']
priceTotal= freightAmount+price
print(buyerAddressId)

case_list2 = [
    (buyerAddressId,1,priceTotal,shopId,"",skuId,num,price,"","",freightAmount, True)
]

@allure.feature('下订单并发起支付')
@allure.description('下订单并发起支付')
@allure.story('下订单并发起支付')
@allure.title('下订单并发起支付')
@pytest.mark.parametrize("buyerAddressId,payType,priceTotal,shopId,remark,skuId,num,price,hideRoomId,guideCode,freightAmount,err",case_list2)
def test_ordercreate (buyerAddressId,payType,priceTotal,shopId,remark,skuId,num,price,hideRoomId,guideCode,freightAmount,err):
    res_2= create.order_create(buyerAddressId,payType,priceTotal,shopId,remark,skuId,num,price,hideRoomId,guideCode,freightAmount,)
    log.debug("返回结果：" + str(res_2))
    assert res_2['success'] == err


    if res_2['success']:
        payOrderId = res_2['object']['payOrderId']
        payType=1
        openId = 'oYXqr5d65Xzh9dZ11udS8Rb1ThfM'
        paymentChannelCode=100
        #支付
        res_3 = pay.orderpay(payOrderId,payType,openId,paymentChannelCode)
        log.debug("返回结果：" + str(res_3))
        assert res_2['success'] == err

        #列表
        res = page.orderpage("WAIT_FOR_PAY", 0, 20)

        #取消交易
        if res['object']['list']:
            orderCode = res['object']['list'][0]['orderCode']
            res_3 = cancel.ordercancel(orderCode)
            log.debug("返回结果：" + str(res_3))
            assert res_3['success'] == err

        else:
            log.error("无待支付订单")
    else:
        log.error("下单失败")