#!/usr/bin/env python
# -*- coding:utf8 -*-
import time
import pickle
import os
from conf import settings
from src import identifier


class BaseModel:
    def save(self):
        file_path = os.path.join(self.db_path, str(self.nid))
        pickle.dump(self, open(file_path, "wb"))

    @classmethod
    def get_all_obj_list(cls):
        ret = []
        for filename in os.listdir(cls.db_path):
            file_path = os.path.join(cls.db_path, filename)
            ret.append(pickle.load(open(file_path, 'rb')))
        return ret


class Admin(BaseModel):
    db_path = settings.ADMIN_DB_DIR

    def __init__(self, username, password):
        self.nid = identifier.AdminNid(self.db_path)
        self.username = username
        self.password = password
        self.create_time = time.strftime("%Y-%m-%d")

    @staticmethod
    def login():
        try:
            name = input("请输入用户名：").strip()
            password = input("请输入密码：").strip()
            for obj in Admin.get_all_obj_list():
                if obj.username == name and obj.password == password:
                    status = True
                    error = ''
                    data = '\033[45;1m登录成功\033[0m'
                    break
            else:
                raise Exception('\033[43;1m用户名或密码错误\033[0m' %name)
        except Exception as e:
            status = False
            error = str(e)
            data = ''
        return {"status": status, "error": error, "data": data}


class School(BaseModel):
    db_path = settings.SCHOOL_DB_DIR

    def __init__(self, name, addr):
        self.nid = identifier.SchoolNid(self.db_path)
        self.name = name
        self.addr = addr
        self.create_time = time.strftime("%Y-%m-%d")
        self.__income = 0

    def __str__(self):
        return self.name
