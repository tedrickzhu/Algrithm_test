#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:sogou20190916.py
#time:2019/9/16 下午7:00

import sys

line = sys.stdin.readline().strip().split(",")
array = [int(i) for i in line]
typedict = {}
for i in array:
    if i in typedict.keys():
        continue
    else:
        typedict[i]=i
count = 0
for key in typedict.keys():
    count = count+typedict[key]
count = count+len(typedict)
print(count)


import sys

data_nums = int(sys.stdin.readline().strip())
dataAraay = []
data_i = 0
while data_i<data_nums:
    nmline = sys.stdin.readline().strip().split()
    n = int(nmline[0])
    m = int(nmline[1])
    count = 0
    usefulstartlines = []
    usefulendlines = []
    while count<m:
        line = sys.stdin.readline().strip().split()
        intline = [int(line[0]),int(line[1])]
        if 1 in intline:
            usefulstartlines.append(intline)
        elif n in intline:
            usefulendlines.append(intline)
        count+=1
    dataAraay.append([[n,m],usefulstartlines,usefulendlines])
    data_i+=1
result = []
for i in range(len(dataAraay)):
    data = dataAraay[i]
    n = data[0][0]
    m = data[0][1]
    startlines = data[1]
    endlines = data[2]
    isOK = False
    for line1 in startlines:
        for lineN in endlines:
            if (lineN[0] in line1) or (lineN[1] in line1):
                isOK = True
                break
        if isOK:
            break
    if isOK:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")



def timu():
    line = sys.stdin.readline().strip().split()
    n = int(line[0])
    m = int(line[1])
    tempdict = {}
    for i in range(n):
        tempdict[i] = 0
    mcircle = []
    while len(mcircle) < m:
        part = sys.stdin.readline().strip().split()
        l = int(part[0])
        r = int(part[1])
        mcircle.append((l, r))
    # 最后一次赋值有效，可以逆着赋值
    # for i in range(len(mcircle)):
    #     circle = mcircle[i]
    #     for k in range(circle[0],circle[1]+1):
    #         array[k] = i+1
    resdict = {}
    k = len(mcircle) - 1
    while k >= 0 and len(tempdict) > 0:
        circle = mcircle[k]
        for i in range(circle[0], circle[1] + 1):
            try:
                tempdict[i] = 0
                tempdict.pop(i)
                resdict[i] = k + 1
            except:
                continue
        k -= 1
    print(tempdict, resdict)
    sum = 0
    for j in range(len(resdict)):
        sum = sum + j * resdict[j]

    print(sum % 100000009)
# 5 3
# 2 3
# 1 2
# 1 1



