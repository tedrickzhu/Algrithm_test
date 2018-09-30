#encoding=utf-8

#将两个有序的数组整理成一个有序的数组，然后，找到这个新的有序数组的中值，如果是奇数个数，则恰好有一个中位数，如果是偶数个，则取两个中位数的均值

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,9,9,9,9]
newarray = []

i = 0
j = 0
while i<len(nums1)	and j<len(nums2):
	a = nums1[i]
	b = nums2[j]
	if a < b:
		newarray.append(a)
		i +=1
	else:
		newarray.append(b)
		j +=1
while i<len(nums1):
	newarray.append(nums1[i])
	i+=1
while j<len(nums2):
	newarray.append(nums2[j])
	j+=1

n = len(newarray)
h = int(n/2)
if n%2 ==0:
	median = (newarray[h-1]+newarray[h])/2.0
else:
	median = newarray[h]

print(median)

