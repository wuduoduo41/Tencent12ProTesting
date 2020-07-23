#!D:\soft\JetBrains\program\other
#-*-coding:utf-8 -*-
# @Time:2020/7/22 21:52
# @Author：anita wu
# @File:search.py
from time import sleep

from app.page_xueqiu.base_page import BasePage


class Search(BasePage):
    

    def search(self,name):
        self._params['name'] = name
        self.steps()


    def add_target(self,name):
        self._params['name'] = name
        self.steps()


    def is_choose(self,name):
        self._params['name'] = name
        if self.steps():
            return True

    def reset(self,name):
        self._params['name'] = name
        return self.steps()
