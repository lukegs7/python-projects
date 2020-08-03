#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 10:44 下午
# @Author  : lukegs7
# @File    : util.py
# @Software: PyCharm

import time

def timestamp2date(timestamp):
    # 格式化时间
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))


def str_of_size(size):
    def strofsize(integer, remainder, level):
        if integer >= 1024:
            remainder = integer % 1024
            integer //= 1024
            level += 1
            return strofsize(integer, remainder, level)
        else:
            return integer, remainder, level

    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    integer, remainder, level = strofsize(size, 0, 0)
    if level+1 > len(units):
        level = -1
    return ( '{}.{:>03d} {}'.format(integer, remainder, units[level]) )
