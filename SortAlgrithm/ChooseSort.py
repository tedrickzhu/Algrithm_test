#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-22
# @Author  : zhengyi
# @File    : ChooseSort.py
# @Software: PyCharm
'''
算法描述
n个记录的直接选择排序可经过n-1趟直接选择排序得到有序结果。具体算法描述如下：

初始状态：无序区为R[1..n]，有序区为空；
第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。
该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，
使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
n-1趟结束，数组有序化了。

核心思想：每次选择一个最小的放到已排好序的数组的尾部，依次循环

'''

def choose_sort(array):
	for i in range(len(array)):
		minIndex=i
		for j in range(i+1,len(array)):
			if array[j]<array[minIndex]:
				minIndex = j
		array[i],array[minIndex]=array[minIndex],array[i]
	return array
	pass

data =[9,4,6,2,7,3,8,5,2,1]
print(choose_sort(data))
