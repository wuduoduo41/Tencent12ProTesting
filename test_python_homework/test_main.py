#!D:\soft\JetBrains\program\other
# -*-coding:utf-8 -*-
# @Time:2020/5/14 22:27
# @Author：anita wu
# @File:test_main.py
import pytest
import yaml


# 要求：-99 ~ 99中的两位整数或者浮点数相加相乘相除相减

def steps():
    with open('./data/steps.yml') as f:
        return yaml.safe_load(f)


class TestMain:

    def setup_class(self):
        print("这是一个简易计算器，您可以使用加减乘除")

    def teardown_class(self):
        print("正在关闭计算器……")

    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./data/mydata.yml"))["add"])
    def calc_add(self, a, b, expect):
        for step in steps():
            if step == 'add':
                try:
                    result = a + b
                    assert result == expect

                except TypeError:
                    print('出现了TypeError')


    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./data/mydata.yml"))["sub"])
    def calc_sub(self, a, b, expect):
        for step in steps():
            if step == 'sub':
                result = a - b
                assert result == expect

    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./data/mydata.yml"))["mul"])
    def calc_mul(self, a, b, expect):
        for step in steps():
            if step == 'mul':
                result = a * b
                assert result == expect

    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./data/mydata.yml"))["div"])
    def calc_div(self, a, b, expect):
        for step in steps():
            if step == 'div':
                result = a / b
                assert result == expect
