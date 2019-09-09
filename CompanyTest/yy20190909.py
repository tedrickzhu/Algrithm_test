#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:yy20190909.py
#time:2019/9/9 下午7:16

import sys

'''
业务理解分析：
        1，数据库中已存有巨量的数据，同时每天依然会新到100TB的数据，
        但是新到的100TB数据其中某些已经在数据库中存在，属于重复数据，另外一些是数据库中没有的，属于新增数据
        2，将新增数据存入库中，重复数据舍弃

解决思路分析：
        1，处理海量数据，传统的关系型数据库已经远远不能满足需求，所以需要使用以Hadoop，HBASE，等为基础的大数据管理技术，
        建立合适大小的服务器集群。
        2，每天新接收到的100TB数据，不可能直接放入内存中实时处理，所以，将数据处理过程拆分成两大模块，
        第一块，一个任务或者服务负责将源源不断到来的数据直接存储下来，直接存入数据仓库，
        此数据仓库并非最终数据仓库，而是一个数据的临时停靠点。
        第二个模块，另一个任务或者服务，不断地从临时仓库中读出数据，与最终仓库的数据做比较，
        判断是否是新数据，新数据则入库，重复数据则舍弃
        3，任务一，直接将源源不断到来的数据直接存储到临时数据仓库
        4，任务二，判断是否是新数据，基于海量数据的比较，一般需要用到搜索引擎，比如基于Lucene的solo引擎，
        利用搜索引擎技术判断数据仓库中是否含有此条数据，若没有检索到，则为新数据，否则，为重复数据，丢弃。
        ​同时，这里的数据检索技术可能是一个难点，如何在海量数据中快速的检索出目标数据，
        除了常用的索引技术，可以使用其他技术，如知识图谱等，提升检索效率。
'''

array = sys.stdin.readline().strip()
i = 0
while i < len(array) - 1:
    deletelast = False
    j = i+1
    while j<len(array):
        if array[j]>array[i]:
            deletelast = True
        elif array[i] == array[j]:
            if deletelast:
                if i == len(array) - 1:
                    array = array[0:len(array) - 2]
                else:
                    array = array[0:j] + array[j + 1:len(array)]
                j-=1
            else:
                if i == 0:
                    array = array[1:len(array)]
                elif i == len(array) - 2:
                    array = array[0:len(array) - 1]
                else:
                    array = array[0:i] + array[i + 1:len(array)]
                i -= 1
                break

        j+=1
    i += 1
res = ""
for i in array:
    res = res + i
print(res)


def timu3():
    line = sys.stdin.readline().strip().split()
    n = int(line[0])
    m = int(line[1])
    array = []

    while len(array) < n:
        num = sys.stdin.readline().strip()
        array.append(num)

    res = array[m:len(array)] + array[0:m]
    restr = ""
    for i in range(len(res)):
        if i < len(res) - 1:
            restr = restr + res[i] + " "
        elif i == len(res) - 1:
            restr = restr + res[i]
    print(restr)

def timu1():
    line = sys.stdin.readline().strip().split()
    array = line[0].split("->")
    n = int(line[1])

    if n < len(array) and n > 1:
        res = array[0:(len(array) - n)] + array[(len(array) - n + 1):len(array)]
        restr = ""
        for i in range(len(res)):
            if i < len(res) - 1:
                restr = restr + res[i] + "->"
            elif i == len(res) - 1:
                restr = restr + res[i]
        print(restr)
    elif n == len(array):
        res = array[1:len(array)]
        restr = ""
        for i in range(len(res)):
            if i < len(res) - 1:
                restr = restr + res[i] + "->"
            elif i == len(res) - 1:
                restr = restr + res[i]
        print(restr)

    elif n == 1:
        res = array[0:len(array) - 1]
        restr = ""
        for i in range(len(res)):
            if i < len(res) - 1:
                restr = restr + res[i] + "->"
            elif i == len(res) - 1:
                restr = restr + res[i]
        print(restr)