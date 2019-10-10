#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:telecom20190918.py
#time:2019/9/18 下午8:45

import sys

line = sys.stdin.readline().strip().split(";")
data1 = line[0]
data2 = line[1]
if len(data1)==len(data2):
    locdict1 = {}
    locdict2 = {}
    for k in range(0,len(data1)):
        try:
            locdict1[data1[k]] = locdict1[data1[k]].append(k)
        except:
            locdict1[data1[k]] = [k]
        try:
            locdict2[data2[k]] = locdict2[data2[k]].append(k)
        except:
            locdict2[data2[k]] = [k]
    if len(locdict1)==len(locdict2):
        for key in locdict1.keys():
            isOK = False
            for ky in locdict2.keys():
                if locdict1[key]==locdict2[ky]:
                    isOK = True
                    break
            if isOK is False:
                print(False)
        print(True)
    else:
        print(False)
else:
    print(False)


def timu3():
    line = sys.stdin.readline().strip().split(",")
    num0 = int(line[0].split("[")[1])
    numN = int(line[len(line) - 1].split("]")[0])
    data = [num0]
    for i in range(1, len(line) - 1):
        data.append(int(line[i]))
    data.append(numN)
    print(data)
    maxSum = -99999999
    start = 0
    while start < len(data):
        currsum = 0
        for k in range(start, len(data)):
            currsum = currsum + data[k]
        if currsum > maxSum:
            maxSum = currsum
        start += 1
    last = len(data)
    while last > 0:
        currsum = 0
        for k in range(0, last):
            currsum = currsum + data[k]
        if currsum > maxSum:
            maxSum = currsum
        last -= 1
    print(maxSum)


def timu1():
    nk = int(sys.stdin.readline().strip())
    data = sys.stdin.readline().strip().split()
    countdict = {}
    for i in data:
        try:
            countdict[i] = countdict[i] + 1
        except:
            countdict[i] = 1
            continue
    print(countdict)
    for key in countdict.keys():
        if countdict[key] == 1:
            print(key)
            break

