#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:yongyou20190911.py
#time:2019/9/11 下午3:02

import random

def timu1():
    import sys
    import re

    line = sys.stdin.readline().strip().split()
    n = int(line[0])
    m = int(line[1])
    n_rules = []
    iplist = []
    while len(n_rules) < n:
        part = sys.stdin.readline().strip().split(".")
        patern = ""
        for i in range(len(part)):
            if i < len(part) - 1:
                if part[i] == "*":
                    patern = patern + "(.*)."
                else:
                    patern = patern + str(part[i]) + "."
            else:
                if part[i] == "*":
                    patern = patern + "(.*)"
                else:
                    patern = patern + str(part[i])
        n_rules.append(patern)
    while len(iplist) < m:
        iplist.append(sys.stdin.readline().strip())

    res = ""
    for i in range(len(iplist)):
        ip = iplist[i]
        ismatch = 0
        for rule in n_rules:
            if re.search(rule, ip):
                ismatch = 1
                break
        if i < len(iplist) - 1:
            res = res + str(ismatch) + " "
        else:
            res = res + str(ismatch)
    print(res)

def timu():
    line = input().split(",")
    p = int(line[0].split()[2])
    array = []
    score = 0
    for i in range(1, len(line)):
        if i == 1:
            array.append(int(line[i].split("[")[1]))
        elif i == len(line) - 1:
            array.append(int(line[i].split("]")[0]))
        else:
            array.append(int(line[i]))
    array.sort()
    if len(array) < 3:
        for k in array:
            if p >= k:
                score += 1
        print(score)
    else:
        pre = 0
        last = len(array) - 1
        while pre <= last:
            if p >= array[pre]:
                score += 1
                p -= array[pre]
                pre += 1
            elif p < array[last]:
                score -= 1
                p += array[last]
                last -= 1
        print(score)

def getPosition(nums,x):

    start = 0
    end = len(nums)-1
    while start<=end:
        currentPos = int((start+end)/2)
        if nums[currentPos]<x:
            start = currentPos+1
            end = end
        elif nums[currentPos]>x:
            start = start
            end = currentPos-1
        elif nums[currentPos]==x:
            return (currentPos,currentPos+1)
    return (end,start)

def resetList(head,x):
    pre = None
    prePoint = None
    last = None
    lastPoint = None
    currentPoint = head

    while currentPoint is None:
        if currentPoint.data <x:
            if pre is None:
                pre = currentPoint
                prePoint = currentPoint
            else:
                prePoint.next = currentPoint
                prePoint = prePoint.next
        else:
            if last is None:
                last = currentPoint
                lastPoint = currentPoint
            else:
                lastPoint.net = currentPoint
                lastPoint = lastPoint.next
        currentPoint= currentPoint.next

    return pre,last

class node:
    data = None
    next = None

def timu2():
    head = node
    head.data = 10
    head.next = None
    print(head.data)
    p = head
    for i in range(10):
        newnode = node
        newnode.data = int(random.randint(0,9))*10+i
        newnode.next = None
        p.next = newnode
        p = p.next
    print(head.data)
    pre,last = resetList(head,30)
    print(pre)
    print(last)

def printPic(length_list):
    for raw in length_list:
        raw_str = ""
        for i in range(raw):
            raw_str=raw_str+"*"
        print(raw_str)

if __name__ == '__main__':

    lenght_list = [1,3,5,7,5,3,1]
    printPic(lenght_list)