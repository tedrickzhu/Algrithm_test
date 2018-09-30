#encoding=utf-8
#问题描述，寻找最大子串，最大子串的定义，最大连续无重复元素的子串
#若已发现一个长度为n的子串substr,在发现 n+1个字符时，第n+1个字符和substr中的第K个字符相同，则检索回溯到k+1位置为起始点，重新开始，记录串的位置，以此来确定每次检索的起始点以及最终子串的长度

s = 'dvdf'
#s = 'abcdabcdefdeaf'

maxsub = ''
maxlength = 0
tmpsubstring = ''
tmpsubstart = 0

if len(s)>0:
	#maxsub = s[0]
	#maxlength = 1
	#tmpsubstring = s[0]
	i = 0
	while i <len(s):
		print('this is i',i)
		char = s[i]    
		if char not in tmpsubstring:
			tmpsubstring = tmpsubstring + char
		elif char in tmpsubstring:
			print('this is temsub,char',tmpsubstring,char)
			if len(tmpsubstring)>maxlength:
				maxsub = tmpsubstring
				maxlength = len(tmpsubstring)	
			for k in range(len(tmpsubstring)):
				if char == tmpsubstring[k]:
					i = tmpsubstart+k+1
					tmpsubstart = tmpsubstart+k+1
					print(k,i)
			tmpsubstring = s[i]
		i+=1
		if len(tmpsubstring)>maxlength:
				maxsub = tmpsubstring
				maxlength = len(tmpsubstring)
	maxlenth = len(maxsub)
	
else:
    print(0,0)

print(maxsub,maxlength)
