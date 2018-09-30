#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-22 上午10:35
# @Author  : zhuzhengyi
# @File    : QuickSort.py
# @Software: PyCharm

#method 1,use lamda function

quicksort1 = lambda array: array if len(array) <= 1 else quicksort1(
	[item for item in array[1:] if item <= array[0]]) + [array[0]] + quicksort1(
	[item for item in array[1:] if item > array[0]])

#method 2 ,normal recursion function,use new array as temp

def quicksort2(nums):
    if len(nums) <= 1:
        return nums
    # 左子数组
    less = []
    # 右子数组
    greater = []
    # 基准数
    base = nums.pop()
    # 对原数组进行划分
    for x in nums:
        if x < base:
            less.append(x)
        else:
            greater.append(x)
    # 递归调用
    return quicksort2(less) + [base] + quicksort2(greater)

#method 3 ,recursion function ,sort inside the original array

def quicksort3(array,left,right):
	if left<right:
		#mid = partion(array,left,right)
		mid = partition2(array,left,right)
		quicksort3(array,left,mid-1)
		quicksort3(array,mid+1,right)
	pass

def partion(array,left,right):
	key = array[left]
	while left<right:
		while left<right and array[right]>=key:
			right-=1
		array[left]=array[right]
		while left<right and array[left]<=key:
			left+=1
		array[right]=array[left]
	array[left]=key
	return left
	pass
#以右侧的数为基准数
def partition2(array, l, r):
	x = array[r]
	i = l - 1
	for j in range(l, r):
		if array[j] <= x:
			i += 1
			array[i], array[j] = array[j], array[i]
	array[i + 1], array[r] = array[r], array[i+1]
	return i+1
	pass

#method 4

def quicksort4(array,left,right):
	if left >= right:
		return
	low = left
	high = right
	key = array[low]
	while left<right:
		# 从右边开始，将第一个比key小的数移至左侧，然后，右侧指针停留不动，
		# 再从左边开始，将第一个比key大的数移至右侧指针所指的位置，
		# 如此循环，
		while left<right and array[right]>key:
			right -=1
		array[left]=array[right]
		while left<right and array[left]<key:
			left +=1
		array[right]=array[left]
	#一次遍历之后，right和lef指向的是同一个位置
	array[left]=key
	quicksort4(array,low,left-1)
	quicksort4(array,left+1,high)
	pass

#method 5 ,非递归实现快排，python 此处用的为队列，
# 每次排序的起点和终点两个数为一对

def quicksort5(array,l,r):
	if l >= r:
		return
	stack = []
	stack.append(l)
	stack.append(r)
	while stack:
		low = stack.pop(0)
		high = stack.pop(0)
		if high - low <= 0:
			continue
		x = array[high]
		i = low - 1
		#j的取值取不到high，所以for循环外面需要做一次置换，
		# 并且i的最终位置为基准元素前面的那个元素
		for j in range(low, high):
			if array[j] <= x:
				i += 1
				array[i], array[j] = array[j], array[i]
			print('i,j:',i,j)
		array[i + 1], array[high] = array[high], array[i + 1]
		#在原数组上面操作，所以队列中需要保存的是每次需要排序的子数组的起始和终点的位置
		stack.extend([low, i, i + 2, high])

	pass

nums = [6,1,2,7,9,3,4,5,10,8]
print(quicksort1(nums))

print(quicksort2(nums))

nums = [6,1,2,7,9,3,4,5,10,8]
print('\ninit data:',nums)
quicksort3(nums,0,len(nums)-1)
print('quicksort3:',nums)

nums = [6,1,2,7,9,3,4,5,10,11,12,13,8]
print('\ninit data:',nums)
quicksort5(nums,0,len(nums)-1)
print(nums)






