#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:byteDance20190908.py
#time:2019/9/8 下午6:46

import sys


def timu4():
    array = sys.stdin.readline().strip()

    stack = [["", 0]]
    result = []
    while len(stack) > 0:
        node = stack.pop()
        substr = node[0]
        point = node[1]
        if point == len(array) - 1:
            substr = substr + array[point]
            result.append(substr)
        elif point < len(array):
            if array[point] == "1" or (array[point] == "2" and int(array[point + 1]) < 7):
                stack.append([substr + array[point], point + 1])
                stack.append([substr + array[point] + array[point + 1], point + 2])
            else:
                stack.append([substr + array[point], point + 1])
        else:
            result.append(substr)
    for i in result:
        point(i)

def timu3():
    line = sys.stdin.readline().strip().split()
    n = int(line[0])
    m = int(line[1])
    q = int(line[2])
    array = sys.stdin.readline().strip().split()
    circlelist = []
    while len(circlelist) < q:
        line = sys.stdin.readline().strip().split()
        circlelist.append([int(line[0]) - 1, int(line[1]) - 1])

    # print(circlelist)
    for circle in circlelist:
        subarray = array[circle[0]:circle[1] + 1]
        # print(subarray)
        socre = 0
        current = 0
        preIsChar = False
        left = False
        right = True
        while len(subarray) > 0 and current >= 0 and current < len(subarray):
            if preIsChar and (subarray[current] == "<" or subarray[current] == ">"):
                if current == 0:
                    subarray = subarray[1:len(subarray)]
                elif current == len(subarray) - 1:
                    subarray = subarray[0:len(subarray) - 1]
                else:
                    subarray = subarray[0:current] + subarray[current + 1:len(subarray)]
            elif subarray[current] == "<":
                current -= 1
                preIsChar = True
                left = True
                right = False
            elif subarray[current] == ">":
                current += 1
                preIsChar = True
                right = True
                left = False
            elif int(subarray[current]) == 0:
                socre = socre + int(subarray[current])
                if current == 0:
                    subarray = subarray[1:len(subarray)]
                elif current == len(subarray) - 1:
                    subarray = subarray[0:len(subarray) - 1]
                else:
                    subarray = subarray[0:current] + subarray[current + 1:len(subarray)]
            else:
                preIsChar = False
                socre = socre + int(subarray[current])
                subarray[current] = int(subarray[current]) - 1
                if left:
                    current -= 1
                if right:
                    current = current + 1
        print(socre)



def hhhh1_error():
    num = int(input())
    line = input().split()
    array = [int(i) for i in line]
    stack = []
    if len(array) == num:
        start = num - 1
        while start >= 0:
            pcheck = start - 1

            while pcheck >= 0:
                if array[pcheck] >= array[start]:
                    stack.push(array[pcheck])
                    break
                pcheck -= 1
        start -= 1
        print(stack.pop())

    else:
        print(0)

def hhh1():
    num = int(input())
    line = input().split()
    array = [int(i) for i in line]
    dictary = {}
    for i in array:
        dictary[i] = 0
    if len(array) == num:
        start = 0
        while start < num:
            pcheck = start + 1
            currenthigh = -1
            while pcheck < num:
                if array[pcheck] <= array[start] and array[pcheck] > currenthigh:
                    dictary[array[start]] += 1
                    currenthigh = array[pcheck]
                elif array[pcheck] > array[start]:
                    break
                pcheck += 1
            start += 1
        maxnum = [-1, -1]
        for key in dictary.keys():
            if dictary[key] > maxnum[1]:
                maxnum = [key, dictary[key]]
        print(maxnum[0])
    else:
        print(0)

