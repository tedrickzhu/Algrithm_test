#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:tencent20190920.py
#time:2019/9/20 下午8:41


import sys

def isNumbers():
    nums = int(sys.stdin.readline().strip())
    data = []
    while len(data)<nums:
        length = int(sys.stdin.readline().strip())
        numstr = sys.stdin.readline().strip()
        data.append([length,numstr])
    for onestr in data:
        if onestr[0]<11:
            print("NO")
            continue
        else:
            curnumstr = onestr[1]
            prestr = curnumstr[0:len(curnumstr)-10]
            if not "8" in prestr:
                print("NO")
                continue
        print("YES")

def maxTime():
    nums = int(sys.stdin.readline().strip())
    count = 0
    timedata = []
    timedict = {}
    while count<nums:
        lines = sys.stdin.readline().strip().split()
        x = int(lines[0])
        y = int(lines[1])
        timedict[y]=x
        timedata.append(y)
        count+=1
    timedata.sort()
    data = []
    for t in timedata:
        for i in range(timedict[t]):
            data.append(t)
    maxtime = 0
    left = 0
    right = len(data)-1
    while left<right:
        if data[left]+data[right]>maxtime:
            maxtime = data[left]+data[right]
        left+=1
        right-=1
    print(maxtime)

def printMin():
    lines = sys.stdin.readline().strip().split()
    n = int(lines[0])
    k = int(lines[1])
    nnumes = sys.stdin.readline().strip().split()
    data = [int(i) for i in nnumes]
    for j in range(k):
        x = 9999999999
        for y in data:
            if y<x and y!=0:
                x = y
        if x == 9999999999:
            x = 0
        print(x)
        for i in range(len(data)):
            if data[i]!=0:
                data[i]=data[i]-x

def yihuo():
    n = int(sys.stdin.readline().strip())
    nnumesa = sys.stdin.readline().strip().split()
    arraya = [int(i) for i in nnumesa]
    nnumesb = sys.stdin.readline().strip().split()
    arrayb = [int(i) for i in nnumesb]
    allsum = None
    for i in arraya:
        for j in arrayb:
            if allsum is None:
                allsum = i+j
            else:
                allsum = allsum ^ (i+j)
    print(allsum)

def fenzu():
    nums = int(sys.stdin.readline().strip())
    data = []
    while len(data) < nums:
        length = int(sys.stdin.readline().strip())
        numstr = sys.stdin.readline().strip().split()
        numsint = [int(i) for i in numstr]
        data.append([length, numsint])
    for onestr in data:
        array = onestr[1]
        array.sort()
        left = 1
        right = len(array)-2
        suma = array[0]+array[len(array)-1]
        sumb = 0
        last = 0
        while left<right:
            if last == 0:
                sumb=sumb+array[left]+array[right]
                last = 1
            elif last == 1:
                suma=suma+array[left]+array[right]
                last = 0
        print(str(suma)+" "+str(sumb))
fenzu()

# 5
# 1 2 1 0 0
# 1 2 3 0 0
# 7 5
# 5 8 10 3 6 10 8


# 3
# 1 8
# 2 5
# 1 2