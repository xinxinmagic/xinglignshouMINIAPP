# coding:utf-8
import os
import configparser

curpath = "%s/config"%os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cfgpath = os.path.join(curpath, "cfg.ini")
conf = configparser.ConfigParser()
conf.read(cfgpath)


user_id = conf.get("login", "user_id")
user_token = conf.get("login", "user_token")
