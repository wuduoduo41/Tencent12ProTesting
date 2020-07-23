#!D:\soft\JetBrains\program\other
#-*-coding:utf-8 -*-
# @Time:2020/7/22 16:26
# @Author：anita wu
# @File:test_xueqiu.py
import pytest
import yaml

from app.page_xueqiu.app import App
from app.page_xueqiu.search import Search


class TestCaseXueQiu:

    _path= '../data_xueqiu/test_case.yml'

    def setup(self):
        self.app=App()
        self.search=self.app.start().main().goto_market().goto_search()


    def teardown(self):
        self.app.quit()

    @pytest.mark.parametrize('name',yaml.safe_load(open(_path,encoding='utf-8')))
    def test01(self,name):
        self.search.search(name)
       
        if self.search.is_choose(name):
            self.search.reset(name)

        self.search.add_target(name)
        assert self.search.is_choose(name)
        self.search.reset(name)

