#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:qunaw20191016.py
#time:2019/10/16 下午8:01

# import sys

n = int(input())
line = input().split()
data = [int(i) for i in line]
data.sort()
fast = data[0]
data = data[1:]
print(fast*(n-2)+sum(data))


def getList(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1,1]
    lastlist = getList(n-1)
    newlist = [1]
    i = 0
    j = 1
    while j<= len(lastlist)-1:
        newpara = lastlist[i]+lastlist[j]
        newlist.append(newpara)
        i += 1
        j += 1
    newlist.append(1)
    return newlist

def timu1():
    n = int(input())
    paralist = getList(n)
    res = ""
    for i in range(len(paralist)):
        if i == len(paralist) - 1:
            res = res + str(paralist[i])
        else:
            res = res + str(paralist[i]) + " "
    print(res)
timu1()