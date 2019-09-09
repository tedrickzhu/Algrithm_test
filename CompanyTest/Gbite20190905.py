#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:Gbite20190905.py
#time:2019/9/5 下午8:21

import sys

fastr = "abcdacd"
substr = "ad"
# 读取第一行的n
# line = sys.stdin.readline().strip().split()
# fastr = line[0]
# substr = line[1]

tmpstr = fastr
res = []
startlist = []
while tmpstr.find(substr[0])>=0:
    index = tmpstr.find(substr[0])
    startlist.append(index)
    if index==0:
        tmpstr = "-"+tmpstr[1:len(tmpstr)]
    elif index==len(tmpstr):
        tmpstr = tmpstr[0:index]+"-"
    else:
        tmpstr = tmpstr[0:index]+"-"+tmpstr[index+1:len(tmpstr)]
for start in startlist:
    oneres = []
    fai =start
    subi = 0
    while fai<len(fastr) and subi <len(substr):
        if fastr[fai]==substr[subi]:
            oneres.append(fai)
            fai=fai+1
            subi=subi+1
        else:
            fai=fai+1
    if len(oneres)==len(substr):
        res.append(oneres)
maxstart = 0
for oneres in res:
    if oneres[0]>maxstart:
        maxstart = oneres[0]
print(maxstart)

