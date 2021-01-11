# coding:utf-8
"""
数据库配置
"""
import psycopg2
import redis


class DataLoader:
    def __init__(self, env):
        self.env = env

    def sql_connect(self,type,sql):
        # 连接数据库
        base = self.env.pg_common
        user = self.env.pg_common_user
        if type =="common":
            base = self.env.pg_common
            user = self.env.pg_common_user
        elif type =="user":
            base = self.env.pg_user
            user = self.env.pg_user_user
        elif type=="item":
            base=self.env.pg_item
            user =self.env.pg_item_user
        elif type=="shop":
            base=self.env.pg_shop
            user =self.env.pg_shop_user
        elif type=="trade":
            base=self.env.pg_trade
            user =self.env.pg_trade_user
        else:
            print("配置需增加新的数据库")

        self.sql_conn = psycopg2.connect(
            "dbname='%s' user='%s' host='%s' password='%s'" % (base, user, self.env.pg_host, self.env.pg_password))
        # 使用cursor()方法获取操作游标
        self.cur = self.sql_conn.cursor()
        result = self.cur.execute(sql)
        # # 提交修改
        # com = sql_conn.commit()
        # # 回滚
        # roll = sql_conn.rollback()
        # # 关闭连接
        # clo = sql_conn.close()

        # 连接redis
        self.redis_conn = redis.Redis(
            host=self.env.redis_host,
            port=self.env.redis_port,
            password=self.env.redis_cridential,
            db=self.env.redis_db)


