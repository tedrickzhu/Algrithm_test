#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-26 下午8:04
# @Author  : zhuzhengyi
# @File    : isSubstring.py
# @Software: PyCharm

'''
两个字符串s和t,回答t是否是s的子序列,输入子序列不要求在原串中是有序的(相邻的)，
例如：原字符串为abc,则它的子序列有{空串，a，b，c，ab，ac，bc，abc}8种。

假设s=abcdefgh,t1=beh,t2=bea,t3=bex。则t1是子串，t2,t3不是

以t为基准，在s中找到t的第一个字符，假设为位置i，从i的位置开始往后继续找t的第二个字符，
依次寻找，直至t中的字符全部找到，或者s中已无未访问的元素。

时间复杂度为O(n+m)

'''

def isSubstring(s,t):

	pass