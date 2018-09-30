
a = -123456
b = str(a)

print(len(b))
length = len(b)
print(b[1])
c = None
if b[0]=='-':
	c = '-'
	print(b[1:length])

	b = b[1:length]
for i in range(len(b)-1,-1,-1):
	print(b[i])
	if c is None:
		c = b[i]
	else:
		c = c+b[i]

print(type(c),c)
d = int(c)
print(type(d),d)

print(2**31-1,-2**31)


