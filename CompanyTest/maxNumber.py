#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:maxNumber.py
#time:2019/8/20 下午3:32


def parseArrary(n,data):
    maxdata=[]
    for i in range(0,n):
        smallcount = 0
        for j in range(1,n):
            if data[j][0]>data[i][0] and data[j][1]>data[i][1]:
                #有数据比data[i]大，所以data[i]不是大数
                break
            else:
                #如果不是则统计不在data[i]大数域内的数的个数
                smallcount = smallcount+1
        #除自身外其他所有是数都不在data[i]的大数域内，则data[i]是大数
        if smallcount==n-1:
            maxdata.append(data[i])
    return maxdata

def maxNum():
    data = []
    n = input()
    n = int(n)
    count = 0
    while count < n:
        line = input()
        count = count + 1
        coup = line.split(' ')
        data.append([int(coup[0]), int(coup[1])])
    maxdata = parseArrary(n, data)
    for coup in maxdata:
        print(str(coup[0]) + ' ' + str(coup[1]) + '\n')

def maxSub():
    data = []
    n = input()
    n = int(n)
    line = input()
    coup = line.split(' ')
    for i in coup:
        data.append(int(i))
    if len(data)==n:
        data.sort()
        result = []
        currlist = []
        i = len(data)-1
        while i >0:
            currlist.append(data[i])
            result.append(min(currlist)*sum(currlist))
            i = i -1
        print(max(result))

    else:
        print("input error")


# data=[]
# n = input()
# n = int(n)
# line = input()
# coup = line.split(' ')
# for i in coup:
#     data.append(int(i))
# if len(data)==n:
#     data.sort()
#     result = []
#     currlist = []
#     i = len(data)-1
#     while i >=0:
#         currlist.append(data[i])
#         result.append(min(currlist)*sum(currlist))
#         i = i -1
#     print(max(result))
# else:
#     print("input error")

# n = input()
# if n=="\n":
#     print("return")
# if n =="":
#     print("empty")


# strmaxnum = input()
# asknum = int(input())
# ailist = [0]*asknum
# num=0
# rslist = [0]*asknum
# while True:
#     ailist[num] = int(input())
#     num=num+1
#     if num>asknum-1:
#         break;
# ailist=[8,0,1,10]
# asknum = 4
# strmaxnum ="1000000008001"
# for i in range(asknum):
#     ai= ailist[i]
#     count = 0
#     m=0
#     substr=0
#     while len(str(substr))<len(strmaxnum):
#         substr = m*1000000007+ai
#         substr = str(substr)
#         x = strmaxnum.find(substr)
#         if x>0 :
#             count = count+1
#             substr2 = "0"+substr
#             while len(substr2) < len(strmaxnum):
#                 x2 = strmaxnum.find(substr2)
#                 if x2 > 0:
#                     count=count+1
#             m=m-1
#         m=m+1
#     print(count)
    # rslist[i]=count
    # 1000000008001
    # 1000,000,008,001
    # 4
    # 8
    # 0
    # 1
    # 10

    # 9
    # 39
    # 5
    # 2
# 6
# 3 + 2 + 1 + -4 * -5 + 1


def aaa():
    asknum = int(input())
    biaodashi = input()
    ailist = biaodashi.split(" ")
    if len(ailist) == asknum + asknum - 1:
        canpri = True;
        while canpri:
            canpri = False
            for i in range(len(ailist)):
                if i % 2 == 1:
                    if ailist[i] == "+" and ailist[i - 1] > ailist[i + 1]:
                        prema = False
                        nextma = False
                        if i - 2 < 0:
                            prema = True
                        elif ailist[i - 2] == "+" or ailist[i - 2] == "-":
                            prema = True
                        if i + 2 > len(ailist) - 1:
                            nextma = True
                        elif ailist[+2] == "+" or ailist[i + 2] == "-":
                            nextma = True
                        if prema and nextma:
                            ailist[i - 1], ailist[i + 1] = ailist[i + 1], ailist[i - 1]
                            canpri = True
                    if ailist[i] == "*" and ailist[i - 1] > ailist[i + 1]:
                        prema = False
                        if i - 2 < 0:
                            prema = True
                        elif ailist[i - 2] == "*" or ailist[i - 2] == "-" or ailist[i - 2] == "+":
                            prema = True
                        if prema:
                            ailist[i - 1], ailist[i + 1] = ailist[i + 1], ailist[i - 1]
                            canpri = True
        output = ""
        for i in range(len(ailist)):
            output = output + ailist[i]
        print(output)








# a="asdfghj"
# print(a[1:7])