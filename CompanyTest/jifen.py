#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:jifen.py
#time:2019/8/23 上午11:10


# from scipy import integrate
# import math
# def f(x, n):
#     return math.pow(n,math.pow(1/2,x-1))
# #1,2为积分范围，args为函数中的参数n
# v, err = integrate.quad(f, 1, 2, args = (2))
# print(v)


ailist=[8,0,1,10]
asknum = 4
strmaxnum ="1000000008001"
for i in range(asknum):
    ai= ailist[i]
    count = 0
    m=0
    substr=0
    while len(str(substr))<len(strmaxnum):
        substr = m*1000000007+ai
        substr = str(substr)
        x = strmaxnum.find(substr)
        if x>0 :
            count = count+1
            substr2 = "0"+substr
            while len(substr2) < len(strmaxnum):
                x2 = strmaxnum.find(substr2)
                if x2 > 0:
                    count=count+1
                    substr2 = "0"+substr2
                else:
                    break
            maxlen = len(strmaxnum)
            strmaxnum2 = strmaxnum[0:x]+strmaxnum[x+1:maxlen]
            while len(strmaxnum2) < len(strmaxnum):
                x3 = strmaxnum2.find(substr)
                if x3 > 0:
                    count=count+1
                    strmaxnum2 = strmaxnum2[0:x3] + strmaxnum2[x3 + 1:maxlen]
                else:
                    break
        m=m+1
    print(count)



