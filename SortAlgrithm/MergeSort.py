#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-22 下午7:48
# @Author  : zhuzhengyi
# @File    : MergeSort.py
# @Software: PyCharm



# 一次归并
def merge(array, low, mid, high):
    """
    两段需要归并的序列从左往右遍历，逐一比较，小的就放到
    tmp里去，再取，再比，再放。
    """
    tmp = []
    i = low
    j = mid +1
    while i <= mid and j <= high:
        if array[i] <= array[j]:
            tmp.append(array[i])
            i += 1
        else:
            tmp.append(array[j])
            j += 1
    while i <= mid:
        tmp.append(array[i])
        i += 1
    while j <= high:
        tmp.append(array[j])
        j += 1
    array[low:high+1] = tmp

def merge_sort(array, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(array, low, mid)
        merge_sort(array, mid+1, high)
        merge(array, low, mid, high)

nums = [6,1,2,7,9,3,4,5,10,8]
print('\ninit data:',nums)
merge_sort(nums,0,len(nums)-1)
print('sorted:',nums)