#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:webank20190919.py
#time:2019/9/19 下午4:38

import sys
nm = sys.stdin.readline().strip().split()
n = int(nm[0])
m = int(nm[1])
lines = []
while len(lines)<m:
    xy = sys.stdin.readline().strip().split()
    lines.append([int(xy[0]),int(xy[1])])
lastin = sys.stdin.readline().strip().split()
start = int(lastin[0])
end = int(lastin[1])
condict = {}
unreach = []
read = [start]
for xy in lines:
    try:
        conlist = condict[xy[0]]
        conlist.append(xy[1])
        condict[xy[0]] = conlist
    except:
        condict[xy[0]] = [xy[1]]
    try:
        conlist = condict[xy[1]]
        conlist.append(xy[0])
        condict[xy[1]] = conlist
    except:
        condict[xy[1]] = [xy[0]]
print(condict)
while len(read)>0:
    curr = read[-1]
    read.remove(curr)
    isUnreach = True
    for nextp in condict[curr]:
        if (nextp not in read) and (nextp not in unreach):
            read.append(nextp)
            isUnreach = False
            break
    if isUnreach:
         unreach.append(curr)
unreach.sort()
print(unreach)

# 5 4
# 1 2
# 2 3
# 4 2
# 5 2
# 1 3


def timu2():
    n = int(sys.stdin.readline().strip())
    maxnum = pow(2, n) + 1
    maxlent = 0
    for x in range(0, maxnum):
        tlist = []
        for t in range(0, maxnum):
            if t & x == t:
                tlist.append(t)
        if len(tlist) > maxlent:
            maxlent = len(tlist)
    print(maxlent % 1000000 + 3)


def timu1():
    n = int(sys.stdin.readline().strip())
    sumn = n
    while n > 1:
        sumn = sumn * (n - 1)
        n -= 1
    data = str(sumn)
    last = len(data) - 1
    while last >= 0:
        if int(data[last]) != 0:
            print(data[last])
            break
        last -= 1
