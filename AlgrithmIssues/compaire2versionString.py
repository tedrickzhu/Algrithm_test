# -*- coding: utf-8 -*-
#请用您熟悉的编程语言，编程实现一个比较任意两个软件版本号大小的函数，
# 如 1.2.3a 和 1.2.4b 比较，后者版本号更大，
# 请考虑各种情况，不可以使用系统提供的比较函数。

#分析：考虑使用正则表达式，但是字符串格式可能非常灵活，不便使用，考虑使用规则判断，将常见的格式考虑入内，比较奇怪的则认为格式错误

def Compare2version(version1,version2):
	if version1.find('.') and version2.find('.'):
		list1 = version1.split('.')
		list2 = version2.split('.')
	elif version1.find('-') and version2.find('-'):
		list1 = version1.split('-')
		list2 = version2.split('-')
	else:
		return 'format error'
	for i in range(min(len(list1),len(list2))):
		a = list1[i]
		b = list2[i]
		if a.isdigit() and b.isdigit():
			a = float(a)
			b = float(b)
			if a <b:
				return '后者为新版本'
			elif a>b:
				return '前者为新版本'
			else:
				pass
		elif len(a) == len(b):
			for j in range(len(a)):
				if a[j]<b[j]:
					return '后者为新版本'
				elif a[j] > b[j]:
					return '前者为新版本'
				else:
					pass
		elif len(a) != len(b):
			if a[0].isalpha() and b[0].isalpha():
				if a[0]<b[0]:
					return '后者为新版本'
				elif a[0] > b[0]:
					return '前者为新版本'
				else:
					try:
						a = float(a[1:])
						b = float(b[1:])
						if a < b:
							return '后者为新版本'
						elif a > b:
							return '前者为新版本'
						else:
							pass
					except Exception:
						return 'format error'
			elif a[-1].isalpha() and b[-1].isalpha():
				if a[-1]<b[-1]:
					return '后者为新版本'
				elif a[-1] > b[-1]:
					return '前者为新版本'
				else:
					try:
						a = float(a[:-1])
						b = float(b[:-1])
						if a < b:
							return '后者为新版本'
						elif a > b:
							return '前者为新版本'
						else:
							pass
					except Exception:
						return 'format error'
	pass


if __name__ == '__main__':
	version1 = '4.1.a12'
	version2 = '4.1.a2s3'
	print(float('12')>float('3'))
	print(version1[:-1])
	if version1[1]==version2[1]:

		print(True)
	print(Compare2version(version1,version2))



# __author__ = 'zzy'
#
# import re
#
#
# def versionCompare(v1="1.1.1", v2="1.2"):
# 	v1_check = re.match("\d+(\.\d+){0,2}", v1)
# 	v2_check = re.match("\d+(\.\d+){0,2}", v2)
# 	if v1_check is None or v2_check is None or v1_check.group() != v1 or v2_check.group() != v2:
# 		return "版本号格式不对，正确的应该是x.x.x,只能有3段"
# 	v1_list = v1.split(".")
# 	v2_list = v2.split(".")
# 	v1_len = len(v1_list)
# 	v2_len = len(v2_list)
# 	if v1_len > v2_len:
# 		for i in range(v1_len - v2_len):
# 			v2_list.append("0")
# 	elif v2_len > v1_len:
# 		for i in range(v2_len - v1_len):
# 			v1_list.append("0")
# 	else:
# 		pass
# 	for i in range(len(v1_list)):
# 		if int(v1_list[i]) > int(v2_list[i]):
# 			return "v1大"
# 		if int(v1_list[i]) < int(v2_list[i]):
# 			return "v2大"
# 	return "相等"
#
#
# # 测试用例
# a = '1-1-1'
# print(a.split('.'))
# print(versionCompare(v1="", v2=""))
# print(versionCompare(v1="1.0.a", v2="d.0.1"))
# print(versionCompare(v1="1.0.1", v2="1.0.1"))
# print(versionCompare(v1="1.0.2", v2="1.0.1"))
# print(versionCompare(v1="1.0.1", v2="1.0.2"))
# print(versionCompare(v1="1.0.11", v2="1.0.2"))