#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-26 下午8:36
# @Author  : zhuzhengyi
# @File    : findMissing.py
# @Software: PyCharm

'''
conference:https://www.cnblogs.com/theskulls/p/4943680.html
寻找缺失的数
给出一个包含 0 .. N 中 N 个数的序列，找出0 .. N 中没有出现在序列中的那个数。

样例
N = 4 且序列为 [0, 1, 3] 时，缺失的数为2。

注意
可以改变序列中数的位置。

挑战
在数组上原地完成，使用O(1)的额外空间和O(N)的时间
'''

#个人比较推荐第一个和第四个解法，更加通用

#重新定义一个数组存放排序后的数(计数排序)，空间复杂度和时间复杂度都是O(N)
def findMissing1(array):

	pass

#可以在原始数组上面操作，如何在原始数组上面操作？空间复杂度并且是O(1)
#  i^i = 0 一个数自身的异或等于0
# 需要先保证数组是非递减有序的数列，可以缺失多个数，可以存在重复数
def findMissing2(array):

	pass

#通过求和来找缺失的数
#只适用于缺失一个数的，数列为0到n的共计n个数，所以数列中也不会有重复的数
def fingMissing3(array):
	n = len(array)
	return n * (n + 1) / 2 - sum(array)

#非常独特的想法
def findMissing4( A):
	# write your code here
	n = len(A)
	if A == None or n == 0:
		return 0
	# num0 = A
	for i in range(n):
		while A[i] != i:
			# num0 = A[:]
			if A[i] < 0 or A[i] >= n:
				break
			tmp = A[i]
			A[i] = A[tmp]
			A[tmp] = tmp
		# if n > 6:
		# print 'before:',num0
		# print ' later:',A

	for i in range(n):
		if A[i] != i:
			return i
	return n


if __name__=='__main__':
	nums =[0,1,3,4,5,6]
	print(fingMissing3(nums))
	pass
