#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-27 上午9:44
# @Author  : zhuzhengyi
# @File    : findPrimeNumber.py
# @Software: PyCharm

'''
找到从a到b的范围内的素数
'''
import math.sqrt as sqrt


#2层循环
def findPrime1(a,b):
	result = []

	if a<=2:
		result.append(2)

	for i in range(3, b):
		isPrime = True
		# for j in range(2,i):
		# 	if i%j ==0:
		# 		isPrime = False
		# 		break
		#判断i是否为素数，不需要判断到i，只需要判断到i的平方根即可（乘法的交换律）
		for j in range(2,sqrt(i)):
			if i%j ==0:
				isPrime = False
				break
		if isPrime:
			result.append(i)
	return result
	pass
#利用素数筛选法进行素数的快速查找
# 原理很简单，素数一定是奇数，素数的倍数一定不是素数
#此方法适合寻找从2开始的到某个数范围内的素数，不适合任意范围的求解

#此实现方式可能有问题，与原思路有些不符
def findPrime2(a,b):
	result = []

	if a<=2:
		result.append(2)

	for i in range(a, b):
		isPrime = True
		if i%2 == 0:
			isPrime = False
		else:
			for j in result:
				if i%j ==0:
					isPrime = False
					break
		if isPrime:
			result.append(i)
	return result
	pass

'''
预定义N表示10000，即表示查找10000以内的素数，
首先定义数组prime[]对N以内的数进行标记，奇数存为1，偶数存为0，
最终实现结果为素数的prime值为1，因此将prime[2]赋值为1（2是素数）。
之后利用for循环，对N以内的奇数进行遍历（注意for循环的条件控制），
for里用if判断是否为素数（奇数），
若是，执行内部嵌套的for循环判断该奇数是否为素数，若是则标记为1，若不是则prime置为0，
之后再用if判断是否为素数，若是，则利用循环将该素数的倍数，都标记为0，意在体现，素数的倍数一定不是素数，
注意for循环内部的条件：for(j=2*i;j<N;j+=i)，表示遍历i的倍数，j为i的倍数，这是for循环的一个技巧。
之后遍历输出prime[i]值为1的i值，便达到了素数的筛选法
'''

def findPrime3(num):
	array = []
	for i in range(num+1):
		if i%2==0:
			array.append(0)
		else:
			array.append(1)
	array[2]=1
	for i in range(3,num+1,2):
		if array[i]:#当i为奇数时再判断他是否为素数
			for k in range(2,sqrt(i)):
				if (i%k)==0:
					array[i]=0
			if array[i]:#当i为素数时，所有i的倍数都不是素数
				j = 2 * i
				while j <=num:
					array[j]=0
					j+=i
	result = [2]
	for i in range(3,num+1,2):
		if array[i]:
			result.append(i)
	return result
	pass

if __name__=='__main__':
	print(findPrime1(1,20))
	print(findPrime1(2,20))
	print(findPrime2(3,100))