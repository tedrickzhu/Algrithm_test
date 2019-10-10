#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:yitu20190920.py
#time:2019/9/20 下午7:30

import sys

def caculat(num):
    if num<1:
        return 0
    elif num == 1:
        return 2
    elif num == 2:
        return 7
    else:
        tmp = int(1.0/2.0 + (caculat(num-1)**2)/((caculat(num-2))+0.0))
        if tmp <0:
            return 0
        else:
            return tmp

nums = int(sys.stdin.readline().strip())
data = []
while len(data) < nums:
    data.append(int(sys.stdin.readline().strip()))
for x in data:
    res = caculat(x)
    print(res)


def timu1():
    ncnums = sys.stdin.readline().strip().split()
    n = int(ncnums[0])
    c = int(ncnums[1])
    lines = sys.stdin.readline().strip().split()
    data = [int(i) for i in lines]
    values = [data[0]]
    count = [1]
    for k in range(1, len(data)):
        isNew = True
        for m in range(len(values)):
            if data[k] == values[m]:
                count[m] = count[m] + 1
                isNew = False
                break
        if isNew:
            values.append(data[k])
            count.append(1)
    curMaxcount = 0
    curmaxindex = -1
    sorted = []
    for k in range(len(count)):
        for i in range(len(count)):
            if count[i] > curMaxcount:
                curMaxcount = count[i]
                curmaxindex = i
        if curmaxindex > -1:
            for j in range(curMaxcount):
                sorted.append(values[curmaxindex])
        count[curmaxindex] = 0
        curMaxcount = 0
        curmaxindex = -1

    res = ""
    for i in range(len(sorted)):
        if i == len(sorted) - 1:
            res = res + str(sorted[i])
        else:
            res = res + str(sorted[i]) + " "

    print(res)
