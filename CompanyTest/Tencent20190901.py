#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:Tencent20190901.py
#time:2019/9/1 下午8:05

import sys

# 读取第一行的n
n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip().split()
scores = [int(k) for k in line]
maxscores = 0

while len(scores)>0:
    minscore = min(scores)
    minindex = [i for i in range(n) if scores[i] == minscore]
    for i in minindex:
        # scores.pop(i)
        pre = None
        behind = None
        if i > 0:
            pre = scores[0:i]
        if i < n:
            behind = scores[i + 1:n]
        if pre is not None:
            x = min(pre) * sum(pre)
            if x > maxscores:
                maxscores = x
        if behind is not None:
            x = min(behind) * sum(behind)
            if x > maxscores:
                maxscores = x
    scores.remove(minscore)

print(maxscores)


def test4():
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip().split()
    scores = [int(k) for k in line]
    maxscores = 0

    for i in range(n):
        box = [scores[i]]
        x = min(box) * sum(box)
        if x > maxscores:
            maxscores = x
        for j in range(i + 1, n):
            box.append(scores[j])
            x = min(box) * sum(box)
            if x > maxscores:
                maxscores = x
    i = n - 1
    while i >= 0:
        box = [scores[i]]
        x = min(box) * sum(box)
        if x > maxscores:
            maxscores = x
        j = i - 1
        while j >= 0:
            box.append(scores[j])
            x = min(box) * sum(box)
            if x > maxscores:
                maxscores = x
            j = j - 1
        i = i - 1
    print(maxscores)


def test3():
    # 读取第一行的n
    line = sys.stdin.readline().strip().split()
    n = int(line[0])
    m = int(line[1])
    line = sys.stdin.readline().strip().split()
    box = [int(k) for k in line]
    if sum(box) <= m:
        print(n + 1)
    count = 1
    for i in range(1,n+1):
        count += 1
        if box[i] <n:
            if m>0:
                m=m-1





def test1():
    # 读取第一行的n
    line = sys.stdin.readline().strip().split()
    n = int(line[0])
    m = int(line[1])
    line = sys.stdin.readline().strip().split()
    box = [int(k) for k in line]
    line = sys.stdin.readline().strip().split()
    keys = [int(k) for k in line]
    count = 0
    for b in box:
        for i in range(len(keys)):
            key = keys[i]
            if (b + key) % 2 == 1:
                count = count + 1
                keys.pop(i)
                break
    print(count)

