#!/usr/bin/env python
# -*- coding:utf8 -*-
import time
import pickle
import os
from conf import settings
from src import identifier


class BaseModel:
    def save