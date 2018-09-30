#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-27 上午10:15
# @Author  : zhuzhengyi
# @File    : greedyMonkey.py
# @Software: PyCharm
'''
猴子第一天摘下若干个桃子，当即吃掉一半，不过瘾，又多吃了一个，
第二天早上又将剩下的桃子吃掉一半，又多吃了一个，
以后每天早上都吃掉剩下桃子的一半零一个，
到第十天早上的时候，发现只剩下一个桃子了，问猴子第一天摘下多少个桃子？

分析，采用逆序的思想
10  1
9   （1+1）×2 = 4
8   (4+1)X2 =10
。
。
。
'''

def countNumbers(day):
	num = 1
	for i in range(1,day):
		num = (num+1)*2
	return num

if __name__=='__main__':
	print(countNumbers(10))
