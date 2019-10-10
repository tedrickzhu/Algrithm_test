#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:kuaishou20190928.py
#time:2019/9/28 下午8:00

import sys

def comStone():
    k = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip().split()
    data = [int(i) for i in line]
    data.sort()
    while len(data)>1:
        start = len(data)-1
        combine = data[start]-data[start-1]
        tmp = []
        if start-1>0:
            tmp = data[0:start-1]
        last = len(tmp)-1
        while last>=0:
            if tmp[last]<=combine:
                if last+1<len(tmp):
                    tmp = tmp[0:last+1]+[combine]+tmp[last+1:len(tmp)]
                    break
                elif last+1>=len(tmp):
                    tmp = tmp+[combine]
                    break
            elif last==0:
                tmp = [combine]+tmp
                break
            last-=1
        if len(tmp)==0:
            tmp = [combine]
        data = tmp
    if len(data)>0:
        print(data[0])
    else:
        print()
comStone()



def countSubStr():
    k = int(sys.stdin.readline().strip())
    data = sys.stdin.readline().strip()
    subsum = 0
    laststartk = 0
    lastbegin = 0
    for x in range(len(data)):
        countk1 = 0
        if data[lastbegin]=="0":
            lastbegin = x
            startki = 1
            for j in range(laststartk + 1, len(data)):
                startki += 1
            subsum += startki
            continue
        else:
            for i in range(start,len(data)):
                if data[i] == "1":
                    countk1 += 1
                if countk1 >= k:
                    laststartk = i
                    startki = 1
                    for j in range(i + 1, len(data)):
                        startki += 1
                    subsum += startki
                    break
    return subsum






def maxScoreSum():
    mst = sys.stdin.readline().strip().split()
    n = int(mst[0])
    m = int(mst[1])
    maxresult = 0
    studentsAns = []
    while len(studentsAns)<n:
        ans = sys.stdin.readline().strip()
        studentsAns.append(ans)
    line = sys.stdin.readline().strip().split()
    scores = [int(i) for i in line]
    for i in range(m):
        ansidict = {}
        for ans in studentsAns:
            try:
                ansidict[ans[i]] = ansidict[ans[i]]+1
            except:
                ansidict[ans[i]] = 1
        maxansi = 0
        for key in ansidict.keys():
            if ansidict[key]>maxansi:
                maxansi = ansidict[key]
        maxresult = maxresult+maxansi*scores[i]
    return maxresult

