#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-27 上午10:07
# @Author  : zhuzhengyi
# @File    : find2ndMax.py
# @Software: PyCharm
'''
写一个函数，找出一个整数数组中，第二大的数

分析，两两无交叉的比较，将数组分为较大组和较小组，
在较大组中重复上述过程，直至较大组中只有2个数，则较小的那个即为第二大的数
'''