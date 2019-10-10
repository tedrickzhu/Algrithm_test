#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:tujia20190921.py
#time:2019/9/22 下午8:50


import sys

def viewcity():
    mst = sys.stdin.readline().strip().split()
    citynum = int(mst[0])
    roadnum = int(mst[1])
    viewnum = int(mst[2])
    viewlines = sys.stdin.readline().strip().split()
    vcitys = [int(i) for i in viewlines]
    roaddict = []
    vdcity = []
    vdroad = []
    count = 0
    while count<roadnum:
        lines = sys.stdin.readline().strip().split()
        a = int(lines[0])
        b = int(lines[1])
        c = int(lines[2])
        try:
            roaddict[a] = roaddict[a].append([b,c])
        except:
            roaddict[a] = [[b,c]]
        try:
            roaddict[b] = roaddict[b].append([a,c])
        except:
            roaddict[b] = [[a,c]]
        count+=1
    vdcity.append(vcitys[0])
    isarrive = True
    while len(vdcity)<len(vcitys):
        minlen = 999999999
        mincit = 0
        for city in vdcity:
            linec = roaddict[city]
            for cityc in linec:
                if (cityc[0] in vcitys) and (cityc[0] not in vdcity) and (cityc[1]<minlen):
                    minlen = cityc[1]
                    mincit = cityc[0]
        if mincit!=0:
            vdcity.append(mincit)
            vdroad.append(minlen)
        else:
            isarrive = False
    if isarrive:
        print(sum(vdroad))



def answer():
    mst = sys.stdin.readline().strip().split()
    m = int(mst[0])
    s = int(mst[1])
    t = int(mst[2])
    run = 13
    jump = 50
    alltime = t
    recover = 4
    walked = 0
    while s>0 and t>0:
        if m>=10:
            m = m-10
            t = t-1
            s = s-50
            walked = walked+50
        elif s>=91 and t>=7:
            #跳两次，绝对划算
            need = 20-m
            tim = need/4.0
            if int(tim)<tim:
                tim = int(tim)+1
            t = t-tim
            m = m +tim*4
            m = m - 20
            s = s-100
            walked = walked+100
            t = t-2
        else:
            #jump once is ok
            need = 10 - m
            tim = need / 4.0
            if int(tim) < tim:
                tim = int(tim) + 1
            if tim+1 <= t and (tim+1)*13<50:
                # jump
                t = t - tim
                m = m + tim * 4
                m = m - 10
                s = s - 50
                walked = walked+50
                t = t - 1
            else:
                #run
                t = t-1
                s = s-13
                walked = walked+13
    if s>0 and t<=0:
        print("NO")
        print(walked)
    elif s<=0 and t>=0:
        print("Yes")
        print(alltime-t)
    # print(m,s,t)


