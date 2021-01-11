import requests,json,os,configparser
from config import headerconfig,env

class Login:

    def __init__(self,env):
        self.env =env
        self.header = headerconfig.Platform(env)

    def login(self):
        url = "%s/webapi/customer/user/wechatLoginAndRegister"% self.env.http_base_url
        params = {
            "appId": "wx2d003fcd85961609",
            "unionId": "oMilBt0LTixLYmOcMgLtbSTGWwns",
            "openId": "oYXqr5d65Xzh9dZ11udS8Rb1ThfM",
            "nickName": "11",
            "avatar": "https://thirdwx.qlogo.cn/mmopen/vi_32/oI4uufyjFwlytkewd6pdyQUeP6U1aRibIlGNibvlQYntQPXpd8wULttiaSib9CBSIdXTGBczJvUoFe3N15ibnDyLW4w/132",
            "p": 6
            }
        # content_type = "application/x-www-form-urlencoded"
        content_type = "application/json"
        headers = self.header.http_header(params,content_type)
        res = requests.post(url =url,data=json.dumps(params),headers = headers).content
        res_json = json.loads(res)
        print(res_json)

        curpath = "%s/config"%os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cfgpath = os.path.join(curpath, "cfg.ini")
        print(cfgpath)

        if res_json['success']:
            user_token = res_json['object']['loginVo']['token']
            user_id = str(res_json['object']['loginVo']['userVo']['id'])
            conf = configparser.ConfigParser()
            conf.read(cfgpath, encoding="utf-8")
            sections = conf.sections()
            print(sections)  # 返回list
            conf.set("login", "user_id", user_id)
            conf.set("login", "user_token", user_token)
            conf.write(open(cfgpath, "w"))
        else:
            print("登录失败")

        return res_json

if __name__=="__main__":
    l = Login(env.QA)
    l.login()