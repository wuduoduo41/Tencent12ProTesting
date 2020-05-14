#!D:\soft\JetBrains\program\other
# -*-coding:utf-8 -*-
# @Time:2020/5/14 22:26
# @Author：anita wu
# @File:conftest.py
import pytest


def pytest_configure(config):
    marker_list = ["add", "sub", "mul", "div"]
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )


def pytest_collection_modifyitems(items):
    for item in items:
        if "add" in item.nodeid:
            item.add_marker(pytest.mark.add)

        if "sub" in item.nodeid:
            item.add_marker(pytest.mark.sub)

        if "mul" in item.nodeid:
            item.add_marker(pytest.mark.mul)

        if "div" in item.nodeid:
            item.add_marker(pytest.mark.div)
