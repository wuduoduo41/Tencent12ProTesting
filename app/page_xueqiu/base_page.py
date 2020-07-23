#!D:\soft\JetBrains\program\other
# -*-coding:utf-8 -*-
# @Time:2020/7/22 16:26
# @Author：anita wu
# @File:base_page.py
import inspect
import json

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from app.page_xueqiu.wrapper import handle_black


class BasePage:
    _locator_path = r'../data_xueqiu/locator.yml'
    _params = dict()

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @handle_black
    def find(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    def finds(self, locator, value: str = None):
        elements:list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    def steps(self):
        func_name = inspect.stack()[1].function
        steps = self.yaml_load(self._locator_path)[func_name]

        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace(f'${{{key}}}', value)
        steps = json.loads(raw)

        for step in steps:
            if 'action' in step.keys():
                action = step['action']
                if 'click' == action:
                    self.find(step['by'], step['locator']).click()

                if 'send_keys' == action:
                    self.find(step['by'], step['locator']).send_keys(step['value'])

                if 'text' == action:
                    text = self.find(step['by'], step['locator']).text
                    return text

                if 'len>0' in action:
                    eles = self.finds(step['by'], step['locator'])
                    return len(eles) > 0

    def implicitly_wait(self, num=5):
        self._driver.implicitly_wait(num)

    def yaml_load(self, path):
        # 要记得return；中文要用utf-8
        return yaml.safe_load(open(path, encoding='utf-8'))

    def screenshot(self,path_name):
        self._driver.save_screenshot(path_name)
