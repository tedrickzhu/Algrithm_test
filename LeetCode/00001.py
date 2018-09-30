
nums = [2,7,11,15,19]
target = 21

result = []

for i in range(len(nums)-1):
	factor1 = nums[i]
	for j in range(i+1,len(nums)):
		factor2 = nums[j]
		if factor1+factor2 == target:
			result.append([i,j])

print(result)