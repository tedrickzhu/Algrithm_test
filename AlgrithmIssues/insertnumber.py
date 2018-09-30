#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-26 下午7:47
# @Author  : zhuzhengyi
# @File    : insertnumber.py
# @Software: PyCharm

'''
小有一个长度为n的整数序列,a_1,...,a_n。然后考虑在一个空序列b上进行n次以下操作:
1、将a_i放入b序列的末尾
2、逆置b序列
小易需要你计算输出操作n次之后的b序列。

输入描述:
输入包括两行,第一行包括一个整数n(2 ≤ n ≤ 2*10^5),即序列的长度。
第二行包括n个整数a_i(1 ≤ a_i ≤ 10^9),即序列a中的每个整数,以空格分割。

输出描述:
在一行中输出操作n次之后的b序列,以空格分割,行末无空格。

输入例子:
4
1 2 3 4

输出例子:
4 2 1 3

分析输出结果：
// 1		1
// 12 		21
// 213 		312
// 3124 	4213
// 42135 	53124
// 531246 	642135

当输入为奇数时前半段为奇数递减，后半段为偶数递增
当输入为偶数时前半段为偶数递减，后半段为奇数递增

问题已解
'''

def getNewList(input):

	pass