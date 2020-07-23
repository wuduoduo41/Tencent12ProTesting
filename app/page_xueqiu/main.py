#!D:\soft\JetBrains\program\other
#-*-coding:utf-8 -*-
# @Time:2020/7/22 16:25
# @Author：anita wu
# @File:main.py
from app.page_xueqiu.base_page import BasePage
from app.page_xueqiu.market import Market


class Main(BasePage):

    def goto_market(self)-> Market:
        self.steps()
        # self.find('xpath','//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="行情"]').click()
        return Market(self._driver)
