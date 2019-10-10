#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:netEaseHuyu.py
#time:2019/9/20 下午5:20

'''
500
5
100,-0.05
320,0.05
120,0
20,0.03
80,0.04

'''


import sys

maxNums = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
goods = []
buyed = []
earn = 0
leftMoney = maxNums
while len(goods)<m:
    line = sys.stdin.readline().strip().split(",")
    goods.append([int(line[0]),float(line[1])])

for good in goods:
    curearn = good[0]*good[1]
    if (leftMoney>good[0]) and (curearn>0):
        buyed.append(good)
        earn = earn+curearn
        leftMoney = leftMoney-good[0]
    elif len(buyed)>0:
        for byg in buyed:
            bygearn = byg[0]*byg[1]
            if (curearn > bygearn) and (good[0]-byg[0]<=leftMoney):
                buyed.remove(byg)
                buyed.append(good)
                earn = earn+curearn-bygearn
                leftMoney = leftMoney+byg[0]-good[0]
                break
print(earn)







class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def removeDuplicates(self,head):
        curstart = head
        curcount = 0
        curend = head
        last = head
        while curend:
            if curend.val == curstart.val:
                curcount+=1
            else:
                if curcount>2:
                    curstart = curstart.next
                    curstart.next = curend
                    last.next = None
                curstart = curend
                curcount=1
            last = curend
            curend = curend.next
        if curcount>2:
            curstart = curstart.next
            curstart.next = curend
            last.next = None
        p = head
        res = ""
        while p :
            if p.next == None:
                res=res+str(p.val)
            else:
                res=res+str(p.val)+" "
            p = p.next
        print(res)

def timu2():
    n = int(sys.stdin.readline().strip())
    lines = sys.stdin.readline().strip().split()
    data = [int(i) for i in lines]
    phead = ListNode(data[0])
    last = phead
    for k in range(1, len(data)):
        p = ListNode(data[k])
        last.next = p
        last = last.next
    # while phead:
    #     print(phead.val)
    #     phead = phead.next
    sol = Solution()
    sol.removeDuplicates(phead)

# 10
# 1 2 2 2 3 3 4 5 5 5




def timu1():
    nm = sys.stdin.readline().strip().split()
    n = int(nm[0])
    m = int(nm[1])
    maxyue = 1
    minbei = n * m
    if n == m:
        maxyue = n
        minbei = n
    elif n < m:
        if m % n == 0:
            maxyue = n
            minbei = m
        else:
            halfn = int(pow(n, 0.5))
            for x in range(1, halfn + 1):
                if n % x == 0:
                    y = n / x
                    if m % x == 0:
                        if x > maxyue:
                            maxyue = x
                    if m % y == 0:
                        if y > maxyue:
                            maxyue = y
            for k in range(1, n):
                if (k * m) % n == 0:
                    minbei = k * m
                    break
    elif m < n:
        if n % m == 0:
            maxyue = m
            minbei = n
        else:
            halfm = int(pow(m, 0.5))
            for x in range(1, halfm + 1):
                if m % x == 0:
                    y = m / x
                    if n % x == 0:
                        if x > maxyue:
                            maxyue = x
                    if n % y == 0:
                        if y > maxyue:
                            maxyue = y
            for k in range(1, m):
                if (k * n) % m == 0:
                    minbei = k * n
                    break

    print(str(maxyue) + " " + str(minbei))