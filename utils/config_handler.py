#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/03/20 13:30
# @Author  : liuxinbo
# @Email   : liuxinbo@cmcm.com
# @File    : config_handler.py
import json
import os

base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
file_dir = os.path.join(base_dir, 'config/')


class ConfigHandler(object):

    def __init__(self, path="", filename=""):
        self.filename = "{}{}".format(path, filename)

    def json_load(self):
        with open(self.filename, encoding='utf-8') as f:
            res = f.read()
        dic = json.loads(res)
        return dic

    def json_write(self, dict_str):
        json_str = json.dumps(dict_str, indent=4)
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(json_str)
        return True

    def get_platform_config(self):
        # 读取config
        config_load = ConfigHandler(file_dir, "config.json")
        # 判断数据
        platform_config = config_load.json_load()
        return platform_config

    def get_sql_config(self):
        # 读取config
        config_load = ConfigHandler(file_dir, "config.json")
        # 判断读取正式数据库还是测试数据库
        sql_env = config_load.json_load()["sql_environment"]

        return sql_env

    def get_sql_connect(self):
        # 读取数据库连接配置
        sql_load = ConfigHandler(file_dir, "database.json").json_load()

        return sql_load

    def rep_database(self, link_conf, data_base=None):
        """
        替换数据库名称
        :param link_conf: database.json连接对应key
        :param data_base: 需要替换的数据库名称
        :return: 数据库链接信息
        """
        conf_load = ConfigHandler(file_dir, "database.json").json_load()
        conf = conf_load[link_conf]
        if data_base:
            conf["database"] = data_base
        print(conf)
        return conf


# config.json文件
config_ = ConfigHandler(file_dir, "config.json")
# config.json文件读取json
config_load = ConfigHandler(file_dir, "config.json").json_load()
# 判断读取正式数据库还是测试数据库
connect_env = config_load["sql_environment"]
# database.json文件
connect_ = ConfigHandler(file_dir, "database.json")
# database.json文件读取json
connect_load = ConfigHandler(file_dir, "database.json").json_load()

if __name__ == '__main__':
    connect_.rep_database("online_config", None)
    connect_.rep_database("online_config", "test")
