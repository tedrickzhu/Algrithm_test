#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-22 下午6:18
# @Author  : zhuzhengyi
# @File    : HeapSort.py
# @Software: PyCharm

'''
堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

算法描述
将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区；
将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]；
由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。
不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。
'''

def sift(array, left, right):
	"""调整"""
	i = left      # 当前调整的小堆的父节点
	j = 2*i + 1   # i的左孩子
	tmp = array[i]     # 当前调整的堆的根节点
	while j <= right:    # 如果孩子还在堆的边界内
		if j < right and array[j] < array[j+1]:   # 如果i有右孩子,且右孩子比左孩子大
			j = j + 1                              # 大孩子就是右孩子
		if tmp < array[j]:                         # 比较根节点和大孩子，如果根节点比大孩子小
			array[i] = array[j]                     # 大孩子上位
			i = j                                   # 新调整的小堆的父节点
			j = 2*i + 1                             # 新调整的小堆中I的左孩子
		else:                                       # 否则就是父节点比大孩子大，则终止循环
			break
	array[i] = tmp                                  # 最后i的位置由于是之前大孩子上位了，是空的，而这个位置是根节点的正确位置。


def heap(array):
	n = len(array)
	# 建堆，从最后一个有孩子的父亲开始，直到根节点
	for i in range(n//2 - 1, -1, -1):
		# 每次调整i到结尾
		sift(array, i, n-1)
	# 挨个出数
	for i in range(n-1, -1, -1):
		# 把根节点和调整的堆的最后一个元素交换
		array[0], array[i] = array[i], array[0]
		# 再调整，从0到i-1
		sift(array, 0, i-1)

nums = [6,1,2,7,9,3,4,5,10,8]
print('\ninit data:',nums)
heap(nums)
print('sorted:',nums)