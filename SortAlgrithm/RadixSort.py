#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-25 下午4:12
# @Author  : zhuzhengyi
# @File    : RadixSort.py
# @Software: PyCharm

'''
基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。
有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。
最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。

算法描述
取得数组中的最大数，并取得位数；
arr为原始数组，从最低位开始取每个位组成radix数组；
对radix进行计数排序（利用计数排序适用于小范围数的特点）；

算法分析
基数排序基于分别排序，分别收集，所以是稳定的。但基数排序的性能比桶排序要略差，
每一次关键字的桶分配都需要O(n)的时间复杂度，而且分配之后得到新的关键字序列又需要O(n)的时间复杂度。
假如待排数据可以分为d个关键字，则基数排序的时间复杂度将是O(d*2n) ，当然d要远远小于n，因此基本上还是线性级别的。

基数排序的空间复杂度为O(n+k)，其中k为桶的数量。一般来说n>>k，因此额外空间需要大概n个左右。
'''

#如果数组中包含小数则需要另一种处理逻辑，这里仅考虑整数
def getMax(array):
	return max(array)
	pass

#一个整数
#获得个位数，模10取余，再整除1
#获得十位数，模100取余，再整除10
#获得千位数，模1000取余，再整除100
#。。。

def RadixSort(array):
	#最大数的位数
	maxepoch = len(str(getMax(array)))
	counter = [[] for i in range(10)]
	mod = 10
	dev = 1
	for i in range(maxepoch):
		resultpoint = 0
		mod = mod * pow(10,i)
		dev = dev * pow(10,i)
		for j in range(len(array)):
			bucketvalue = (array[j]%mod)//dev
			counter[bucketvalue].append(array[j])
		for k in range(len(counter)):
			while len(counter[k]) > 0:
				array[resultpoint] = counter[k].pop(0)
				resultpoint += 1
	return array
	pass


if __name__=='__main__':
	nums = [6,1,2,7,9,300,4,5,10,8,12,15,17,17,19,26]
	print('\ninit data:',nums)
	RadixSort(nums)
	print('sorted:',nums)

