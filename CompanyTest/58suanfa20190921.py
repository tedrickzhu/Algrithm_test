#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:58suanfa20190921.py
#time:2019/9/21 下午9:18

import sys

def changEmail():
    email = sys.stdin.readline().strip()
    endindex = email.find("@")
    insert = []
    newemail = ""
    for i in range(int(endindex/4)+1):
        insert.append("M")
        insert.append("A")
        insert.append("S")
        insert.append("K")
    for i in range(endindex):
        if i == endindex-1:
            newemail = newemail+email[i]
        else:
            newemail = newemail+email[i]+insert[i]
    newemail = newemail+email[endindex:len(email)]
    print(newemail)
# changEmail()

# chuangpu@whitehouse.com

def chang():
    num = int(sys.stdin.readline().strip())
    chars = ["'","!","@","#","$","%","^","&","*","(",")","{","}","\\","<",">","?"]
    res = ""

    while int(num/27)>0:
        left = int(num/27)
        right = num%27
        if right>9:
            res = chars[right-10]+res
        else:
            res = str(right)+res
        num = left
    if num > 9:
        res = chars[num - 10] + res
    else:
        res = str(num) + res
    print(res)

def answer():
    lines = sys.stdin.readline().strip().split(",")
    data = [int(i) for i in lines]
    rate = int(data[0])
    nums = len(data)-1
    cal = nums*(rate/100.0)
    youxiunums = int(nums*(rate/100.0))
    if youxiunums < cal:
        youxiunums+=1
    count = 0
    curmax = 0
    while count<youxiunums:
        curmax = max(data)
        data.remove(curmax)
        count+=1
    print(curmax)

answer()
