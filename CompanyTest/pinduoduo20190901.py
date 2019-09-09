#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:pinduoduo20190901.py
#time:2019/9/1 下午3:05

import sys

line = "555503,772867,756893,339138,399447,40662,859037,628085,855723,974471,599631,636153,581541,174761,948135,411485,554033,858627,402833,546467,574367,360461,566480,755523,222921,164287,420256,40043,977167,543295,944841,917125,331763,188173,353275,175757,950417,284578,617621,546561,913416,258741,260569,630583,252845;10"

def test():
    data = line.split(",")
    lastlist = data[-1].split(";")
    num = int(lastlist[1])
    data = data[0:(len(data) - 1)]
    data.append(lastlist[0])
    data = [int(k) for k in data]
    oushu = []
    qishu = []
    for i in data:
        if i % 2 == 0:
            oushu.append(i)
        if i % 2 == 1:
            qishu.append(i)
    oushu.sort(reverse=True)
    qishu.sort(reverse=True)
    # print(oushu)
    # print(qishu)
    res = oushu + qishu
    output = ""
    for j in range(num):
        if j == num - 1:
            output = output + str(res[j])
        else:
            output = output + str(res[j]) + ","

    print(output)

def test2():
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())*2
    data = [0 for i in range(n)]
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        n_m_data = []
        if i%2==0:
            n_m_data = [int(k) for k in line.split()]
        if i%2==1:
            n_m_data = [int(k) for k in line.split()]
        data[i] = n_m_data
    circle = 1

    while circle<=n/2:
        n_data = data[circle-1]
        m_data = data[circle]
        head = 0
        tail = len(m_data)-1
        stack = []
        res = []
        resOp = []
        stack.append([n_data,m_data,res,resOp,0,head,tail])
        output = ["{"]
        while len(stack) > 0:
            c = stack.pop()
            n_data = c[0]
            m_data = c[1]
            res = c[2]
            resOp = c[3]
            j = c[4]
            head = c[5]
            tail = c[6]
            if head <= tail:
                for k in range(j, len(n_data)):
                    if n_data[k] == m_data[head]:
                        stack.append([n_data, m_data, res.append(n_data[k]), resOp.append("l"), k + 1, head + 1, tail])
                        break
                    elif n_data[k] == m_data[tail]:
                        stack.append([n_data, m_data, res.append(n_data[k]), resOp.append("r"), k + 1, head, tail - 1])
                        break
                    else:
                        resOp.append("d")
            elif len(res) == len(m_data):
                path =""
                for i in range(len(resOp)):
                    if i == len(resOp)-1:
                        path = path+resOp[i]
                    else:
                        path = path+i+" "
                output.append(path)
        for pathres in output:
            print(pathres)
        circle = circle+1

# a = []
# print(len(a))
test2()

# 3
# 123
# 3
# 123
# 321
# 45
# 67


def test4():
    nums = input().split()
    n = int(nums[0])
    m = int(nums[1])
    k = int(nums[2])
    data = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            data.append(i * j)
    data.sort(reverse=True)
    print(data[k])
