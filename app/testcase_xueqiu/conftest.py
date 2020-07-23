#!D:\soft\JetBrains\program\other
#-*-coding:utf-8 -*-
# @Time:2020/7/23 22:37
# @Author：anita wu
# @File:conftest.py
import os
import shlex
import signal
import subprocess

import pytest


@pytest.fixture(scope='class',autouse=True)
def record_vedio():
    cmd=shlex.split('scrcpy --record tmp.mp4') #这里的命名需要改成时间，怎么修改？
    p=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print(p)
    yield
    os.kill(p.pid,signal.CTRL_C_EVENT)