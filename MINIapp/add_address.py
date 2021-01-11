# ----------------------- #
# author:zhangxin         #
# time:20210104           #
# ----------------------- #
import requests
import json
from config import headerconfig, env
# from common.logger import Log
from common import logger,encryption



class Addaddress:
    def __init__(self, env):
        self.env = env
        self.log = logger.Log()
        self.header = headerconfig.Platform(env)


    def addaddress(self,addressDetail,cityCode,cityName,districtCode,districtName,nickName,phone,provinceCode,provinceName,streetCode,streetName,wxImport):
        """
         用户添加收货地址
        :param addressDetail:
        :param cityCode:
        :param cityName:
        :param districtCode:
        :param districtName:
        :param nickName:
        :param phone:
        :param provinceCode:
        :param provinceName:
        :param streetCode:
        :param streetName:
        :param wxImport:
        :return:
        """
        url = '%s/webapi/customer/address/add' % self.env.http_base_url
        params = {
            "addressDetail": addressDetail,
            "cityCode": cityCode,
            "cityName": cityName,
            "districtCode": districtCode,
            "districtName": districtName,
            "nickName": nickName,
            "phone": phone,
            "provinceCode": provinceCode,
            "provinceName": provinceName,
            "streetCode": streetCode,
            "streetName": streetName,
            "wxImport":wxImport
}

        # content_type = "application/x-www-form-urlencoded"
        content_type = "application/json"
        headers = self.header.http_header(params,content_type)
        self.log.debug(headers)
        res = requests.post(url=url, data=json.dumps(params), headers=headers).content
        res_json = json.loads(res)
        self.log.debug(res_json)
        return res_json


if __name__ == "__main__":
    l = Book(env.QA)
    res = l.book(1)
    print(type(res))
