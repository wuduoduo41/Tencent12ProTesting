#!D:\soft\JetBrains\program\other
#-*-coding:utf-8 -*-
# @Time:2020/7/22 21:51
# @Author：anita wu
# @File:market.py
from app.page_xueqiu.base_page import BasePage
from app.page_xueqiu.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps()
        # self.find('xpath','//*[@resource-id="com.xueqiu.android:id/action_search"]').click()
        return Search(self._driver)