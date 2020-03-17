#!/usr/bin/env python
# -*- coding:utf8 -*-
from lib import common
import os
import pickle


class Nid:
    def __init__(self, role, db_path):
        role_list = ['admin', 'school', 'teacher', 'course', 'course_to_teacher', 'classes', 'student']

    if role not in role_list:
        raise Exception("用户角色错误，选项：%s" % ','.join(role_list))
    self.role = role
