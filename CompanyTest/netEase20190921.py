#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:netEase20190921.py
#time:2019/9/21 下午3:56

import sys

def answer():
    nm = sys.stdin.readline().strip().split()
    perNums = int(nm[0])
    askNums = int(nm[1])
    data = sys.stdin.readline().strip().split()
    askdata = []
    while len(askdata)<askNums:
        askdata.append(sys.stdin.readline().strip())
    countdict = {}
    for i in data:
        try:
            countdict[i] = countdict[i]+1
        except:
            countdict[i] = 1
    for k in askdata:
        try:
            print(countdict[k])
        except:
            print(0)

def changa():
    n = int(sys.stdin.readline().strip())
    data = []
    while len(data)<n:
        lines = sys.stdin.readline().strip().split()
        abpq = [int(i) for i in lines]
        data.append(abpq)
    for onesam in data:
        a = onesam[0]
        b = onesam[1]
        p = onesam[2]
        q = onesam[3]
        count = 0
        while a+p<b:
            p = p*q
            count +=1
        count+=1
        print(count)

def changewood():
    nums = int(sys.stdin.readline().strip())
    data = []
    while len(data) < nums:
        lines = sys.stdin.readline().strip().split()
        n = int(lines[0])
        m = int(lines[1])
        lined = sys.stdin.readline().strip().split()
        woods = [int(i) for i in lined]
        data.append([n,m,woods])
    for onewod in data:
        n = onewod[0]
        m = onewod[1]
        wod = onewod[2]
        if sum(wod)+m >= n*(n-1)/2:
            print("YES")
        else:
            print("NO")


def jumptoend():
    nums = int(sys.stdin.readline().strip())
    data = []
    while len(data) < nums:
        lines = sys.stdin.readline().strip().split()
        n = int(lines[0])
        m = int(lines[1])
        lined = sys.stdin.readline().strip().split()
        woods = [int(i) for i in lined]
        data.append([n,m,woods])
    for onewod in data:
        n = onewod[0]

        wod = onewod[2]
        isOK = True
        superpower = True
        i = 0
        while i < len(wod):
            isJump = False
            nextk = []
            k = onewod[1]
            while k>0 :
                if i+k<len(wod):
                    nextk.append(wod[i+k])
                    if wod[i]>=wod[i+k]:
                        i+=k
                        isJump = True
                        break
                k-=1
            if isJump:
                continue
            elif superpower:

                maxi = nextk.index(max(nextk))+1
                i+=maxi
                superpower=False
            else:
                isOK = False
                break

        if isOK:
            print("YES")
        else:
            print("NO")
jumptoend()

# 1
# 5 3
# 6 2 4 3 8

# 1
# 5 2
# 1 8 2 3 4

# 1
# 5 3
# 2 2 3 3 1

# 2
# 1 5 7 2
# 3 5 1 2

# 7 4
# 6 2 1 2 6 2 5
# 6
# 5
# 8
# 2