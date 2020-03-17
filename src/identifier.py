#!/usr/bin/env python
# -*- coding:utf8 -*-
from lib import common
import os
import pickle


class Nid:
    def __init__(self, role, db_path):
        role_list = [
            'admin', 'school', 'teacher', 'course', 'course_to_teacher', 'classes', ''
        ]