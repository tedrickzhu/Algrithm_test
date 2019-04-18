#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:findbestsub.py
#time:2019/4/8 下午7:55

s = '2, -2, 7, 6, -8, -10, -5'
charlist = s.split(',')

numlist = []
for char in charlist:
    numlist.append(int(char))
numlist.sort()
substringlist = []
substring = [numlist[0]]
count = numlist[0]
for i in range(1,len(numlist)):
    if count+numlist[i]>count:
        substringlist.append(substring)
        substring=[numlist[i]]
        count = numlist[i]
        continue
    else:
        substring.append(numlist[i])
        count = count + numlist[i]
print(numlist)