# ----------------------- #
#    author:zhangxin      #
#                         #
#      time:20200923      #
#                         #
# ----------------------- #
class Env:
    """
    环境配置
    """
    http_base_url = ""
    redis_host = ""
    redis_port = 6379
    redis_cridential = "youknowthat"
    redis_db = ""
    pg_host = ""
    pg_port = 5432
    pg_user = "syds_user"
    pg_item = "syds_item"
    pg_trade = "syds_trade"
    pg_shop = "syds_shop"
    pg_common = "syds_common"
    pg_user_user = "syds_user_dev"
    pg_item_user = "syds_item_dev"
    pg_trade_user = "syds_trade_dev"
    pg_shop_user = "syds_shop_dev"
    pg_common_user = "syds_common_dev"
    pg_password = ""
    super_username = ""
    super_password = ""
    cloud_user = ""
    cloud_password = ""
    shop_user = ""
    shop_password = ""


class QA(Env):
    http_base_url = "http://10.4.24.93:10010"
    redis_host = "10.4.24.191"
    pg_host = "10.4.24.13"
    pg_password = "syds123"
    super_username = "eleven"
    super_password = "123456"
    cloud_user = "ele01"
    cloud_password = "123456"
    shop_user = "13048052194"
    shop_password = "123456"


class Dev(Env):
    http_base_url = "http://10.4.22.37:10010"
    super_username = "eleven"
    super_password = "123456"
    cloud_user = "ele01"
    cloud_password = "123456"
