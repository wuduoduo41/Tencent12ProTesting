#!D:\soft\JetBrains\program\other
# -*-coding:utf-8 -*-
# @Time:2020/7/23 15:52
# @Author：anita wu
# @File:wrapper.py
import logging
import time

import allure
from selenium.webdriver.common.by import By


def handle_black(func):
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        from app.page_xueqiu.base_page import BasePage
        _black_list = [(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]'),
                       (By.XPATH, "//*[@text='确认']"),
                       (By.XPATH, "//*[@text='确定']"),
                       (By.XPATH, "//*[@text='下次再说']")]
        _max_num = 3
        _error_num = 0

        instance: BasePage = args[0]
        try:
            logging.info('run: ' + func.__name__ + '\n args:\n' + repr(args[1:]) + '\n kwargs:\n' + repr(kwargs))
            element = func(*args, **kwargs)
            _error_num = 0
            instance.implicitly_wait(5)
            return element

        except Exception as e:
            #错误日志收集
            logging.error('element is not found,now handle black list')

            #截图
            name = time.strftime('%Y_%m_%d_%H_%M_%s)')
            instance.screenshot(path_name=f'../photos_xueqiu/{name}.png')

            #将图片转化成二进制文件
            with open(f'../photos_xueqiu/{name}.png','rd') as f:
                content=f.read()

            #关联allure
            allure.attach(content, attachment_type=allure.attachment_type.PNG)

            _error_num += 1
            instance.implicitly_wait(1)
            if _error_num > _max_num:
                raise e

            else:
                for black in _black_list:
                    eles = instance.finds(black)
                    if len(eles) > 0:
                        eles[0].click()
                        return func(*args, **kwargs)
                raise e

    return wrapper
