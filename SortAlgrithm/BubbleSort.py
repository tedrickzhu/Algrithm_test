#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-22
# @Author  : zhengyi
# @File    : BubbleSort.py
# @Software: PyCharm

'''
算法描述
比较相邻的元素。如果第一个比第二个大，就交换它们两个；
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
针对所有的元素重复以上的步骤，除了最后一个；
重复步骤1~3，直到排序完成。
'''

def bubble_sort(data):
	for i in range(len(data)):
		for j in range(len(data)-i-1):
			if data[j]>data[j+1]:
				data[j+1],data[j] = data[j],data[j+1]
	return data
	pass

#改进：如果一趟比较没有发生位置变换，则认为排序完成

def bubble_sort2(data):
	for i in range(len(data)):
		isSwatch = False
		for j in range(len(data)-i-1):
			if data[j]>data[j+1]:
				data[j+1],data[j] = data[j],data[j+1]
				isSwatch = True
		if isSwatch is not True:
			break
	return data

data =[9,4,6,2,7,3,8,5,2,1]
print(bubble_sort(data))
print(bubble_sort2(data))