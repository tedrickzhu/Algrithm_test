#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:360campus20190831.py
#time:2019/8/31 下午7:43


def maxNumSubStr():
    fastr = input()
    length = len(fastr)
    maxnumsubstr = (fastr, 1)
    sublen = length - 1
    dictnary = {}
    while sublen > 0:

        for i in range(0, length):
            if i + sublen <= length:
                substr = fastr[i:i + sublen]
                if substr in dictnary:
                    dictnary[substr] = dictnary[substr] + 1
                else:
                    dictnary[substr] = 1
            else:
                break
        for key in dictnary:
            if dictnary[key] > maxnumsubstr[1]:
                maxnumsubstr = (key, dictnary[key])
        dictnary = {}
        sublen = sublen - 1

    print(maxnumsubstr[1])


def maxNumSubstr2():
    fastr = input()
    length = len(fastr)
    maxnumsubstr = (fastr, 1)
    sublen = 1
    dictnary = {}
    while sublen <= length - maxnumsubstr[1] + 1:
        for i in range(0, length):
            if i + sublen <= length:
                substr = fastr[i:i + sublen]
                if substr in dictnary:
                    dictnary[substr] = dictnary[substr] + 1
                else:
                    dictnary[substr] = 1
            else:
                break
        for key in dictnary:
            if dictnary[key] > maxnumsubstr[1]:
                maxnumsubstr = (key, dictnary[key])
        sublen = sublen + 1
        dictnary = {}

    print(maxnumsubstr[1])

def test2():
    nm = input()
    x = nm.split(" ")
    n = int(x[0])
    m = int(x[1])
    d_list = []
    res = 0
    inputMnums = 0
    while inputMnums < m:
        d_list.append(int(input()))
        inputMnums = inputMnums + 1
    for num in range(1, n + 1):
        i = 0
        isok = True
        while i < len(d_list):
            d = d_list[i]
            if num + d >= 1 or num - d <= n:
                i = i + 1
            else:
                isok = False
        if isok:
            res = res + 1

    print(res)