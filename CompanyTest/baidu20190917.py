#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:baidu20190917.py
#time:2019/9/17 下午7:52

import sys

nmk = sys.stdin.readline().strip().split()
n = int(nmk[0])
m = int(nmk[1])
k = int(nmk[2])

halfk = int(pow(k,0.5))+1
res = []
if n<m:
    for a in range(n-halfk):
        minb = int(m-k/(n-a))
        if minb<0:
            mib = 0
        res.append(a+minb)
else:
    for b in range(m-halfk):
        mina = int(n-k/(m-b))
        if mina<0:
            mina = 0
        res.append(b+mina)
print(min(res))
