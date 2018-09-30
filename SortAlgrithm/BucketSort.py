#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-25 下午1:51
# @Author  : zhuzhengyi
# @File    : BucketSort.py
# @Software: PyCharm

'''
桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。
桶排序 (Bucket sort)的工作的原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，
每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）。

算法描述
设置一个定量的数组当作空桶；
遍历输入数据，并且把数据一个一个放到对应的桶里去；
对每个不是空的桶进行排序；
从不是空的桶里把排好序的数据拼接起来。
'''

#对于每一个单独的桶，需要别的排序算法来辅助排序，此处采用计数排序来辅助
from CountingSort import CountingSort

def getMax(array):
	return max(array)
	pass

def getMin(array):
	return min(array)
	pass

def BucketSort(array):
	minValue = getMin(array)
	maxValue = getMax(array)

	DEFAULT_BUCKET_SIZE = 5
	value_range = 5
	bucketcount = (maxValue-minValue)//value_range + 1
	buckets = [[] for i in range(bucketcount)]
	resultpoint =0
	for i in range(len(array)):
		buckets[(array[i]-minValue)//value_range].append(array[i])
	for k in range(len(buckets)):
		if len(buckets[k])>1:
			CountingSort(buckets[k])
		while len(buckets[k])>0:
			array[resultpoint]=buckets[k].pop(0)
			resultpoint+=1
	return array
	pass


if __name__=='__main__':
	nums = [6,1,2,7,9,3,4,5,10,8,12,15,17,17,19,26]
	print('\ninit data:',nums)
	BucketSort(nums)
	print('sorted:',nums)

'''
class bucketSort(object):
	def insertSort(self, a):
		n = len(a)
		if n <= 1:
			pass
		for i in range(1, n):
			key = a[i]
			j = i - 1
			while key < a[j] and j >= 0:
				a[j + 1] = a[j]
				j -= 1
			a[j + 1] = key

	def sort(self, a):
		n = len(a)
		s = [[] for i in range(n)]
		for i in a:
			s[int(i * n)].append(i)
		for i in s:
			self.insertSort(i)
		return [i for j in s for i in j]

	def __call__(self, a):
		return self.sort(a)


if __name__ == '__main__':
	from random import random
	from timeit import Timer

	a = [random() for i in range(10)]


	def test_bucket_sort():
		bucketSort()(a)


	def test_builtin_sort():
		sorted(a)


	tests = [test_bucket_sort, test_builtin_sort]

	for test in tests:
		name = test.__name__
		t = Timer(name + '()', 'from __main__ import ' + name)
		print(t.timeit(1))
		print(test)
'''
