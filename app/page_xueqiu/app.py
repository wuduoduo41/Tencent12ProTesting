#!D:\soft\JetBrains\program\other
# -*-coding:utf-8 -*-
# @Time:2020/7/22 16:25
# @Author：anita wu
# @File:app.py
import inspect

import yaml
from appium import webdriver

from app.page_xueqiu.base_page import BasePage
from app.page_xueqiu.main import Main


class App(BasePage):

    def start(self):
        if self._driver == None:

            desired_caps:dict
            desired_caps = yaml.safe_load(open(r'D:\soft\JetBrains\Tencent12ProTesting\app\data_xueqiu\caps.yml'))['caps']


            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            self.implicitly_wait(7)

        else:
            self._driver.launch_app()

        return self

    def restart(self):
        pass

    def quit(self):
        self._driver.quit()

    def main(self) -> Main:
        return Main(self._driver)
