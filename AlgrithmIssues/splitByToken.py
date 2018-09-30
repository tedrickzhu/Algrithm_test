#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-26 下午9:07
# @Author  : zhuzhengyi
# @File    : splitByToken.py
# @Software: PyCharm
'''
void strton(constchar* src, const char*token)
假设src是一长串字符，token存有若干分隔符，只要src的字符是token中的任何一个，就进行分割，
最终将src按照token分割成若干单词。找出一种O(n)算法？

提示：查表的方法，将所有的字符串存储在长度为128的数组中，并将作为分隔符的字符位置1，
这样即可用常数时间判断字符是否为分隔符，通过n次扫描，将src分割成单词。

将token中的字符按照ascii码的数字表示方式，用一个长度为128的数组asciiarray表示，
数组的对应位置为1，其他未在token中出现的字符的位置为0

遍历一遍string中的每个字符，通过判断ASCIIarray中，该字符对应的位置的值是否为1判断该字符是否为分隔符。
以此达到线性时间判断字符是否为分隔符，时间复杂度为O(n+m)

'''

#方法一，两个for循环，时间复杂度为O(n*m)
def splitByToken(string):

	pass

#方法二
def splitByToken(string):

	pass