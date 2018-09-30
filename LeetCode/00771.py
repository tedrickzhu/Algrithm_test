
j = 'aA'
s = 'aAAbcdedede'

jlist =[]
for jindex in range(len(j)):
	ji = j[jindex]
	print(ji)
	jlist.append(ji)

print(jlist)
count = 0
for sindex in range(len(s)):
	si = s[sindex]
	if si in jlist:
		count+=1

print('this is the vaule of count:',str(count))