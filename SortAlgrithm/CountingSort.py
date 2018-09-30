#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-24 下午9:08
# @Author  : zhuzhengyi
# @File    : CountingSort.py
# @Software: PyCharm

'''
计数排序不是基于比较的排序算法，其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。

算法描述
找出待排序的数组中最大和最小的元素；
统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。

注意：对于待排序的数不是整数的情况，此种方法不适用

'''

def getMax(array):
	return max(array)
	pass

def getMin(array):
	return min(array)
	pass

def CountingSort(array):
	minValue = getMin(array)
	maxValue = getMax(array)
	#初始化一个计数桶
	bucket = [0 for i in range(maxValue+1)]
	#对每个数计数，并存入相应的桶中
	for i in range(len(array)):
		value = array[i]
		bucket[int(value)] = bucket[int(value)] + 1
	#将数据按照新的顺序重新填入原来的数组
	arraypoint = 0
	for j in range(len(bucket)):
		# count = bucket[j]
		# if count>0:
		# 	for k in range(count):
		# 		array[arraypoint]=j
		# 		arraypoint+=1
		while bucket[j] > 0:
			array[arraypoint]=j
			arraypoint+=1
			bucket[j] -=1
	return array
	pass

if __name__=='__main__':
	nums = [6,1,2,7,9,3,4,5,10,8]
	print('\ninit data:',nums)
	CountingSort(nums)
	print('sorted:',nums)
