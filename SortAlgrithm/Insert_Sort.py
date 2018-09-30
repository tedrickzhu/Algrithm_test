#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-22 上午9:59
# @Author  : zhengyi
# @File    : Insert_Sort.py
# @Software: PyCharm
'''
算法描述
一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：

从第一个元素开始，该元素可以认为已经被排序；
取出下一个元素，在已经排序的元素序列中从后向前扫描；
如果该元素（已排序）大于新元素，将该元素移到下一位置；
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
将新元素插入到该位置后；
重复步骤2~5。

Intro:核心思想是将某个元素插入一个有序的列表中，如果在当前的数组中操作，需要O(1)的空间复杂度
会花费大量的时间在移位操作上
'''
def InsertSort(array):

	for i in range(1,len(array)):
		current = i
		pre_point = current-1
		right_position = False
		while pre_point>=0 and not right_position:
			if array[current]<array[pre_point]:
				array[current],array[pre_point]=array[pre_point],array[current]
				pre_point-=1
				current -=1
			else:
				right_position = True
	return array
	pass

def InsertSort2(array):

	for current in range(1,len(array)):
		current_value = array[current]
		pre_point = current-1
		while pre_point>=0 and array[pre_point]>current_value:
			array[pre_point+1]=array[pre_point]
			pre_point-=1
		#找到位置时，pre_point指向空位置的前一个位置
		array[pre_point+1]=current_value
	return array
	pass

data =[9,4,6,2,7,3,8,5,2,1]
print(InsertSort(data))
print(InsertSort2(data))