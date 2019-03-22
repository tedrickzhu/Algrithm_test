#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:findinmatrix.py
#time:2019/3/20 下午5:10
'''
链接：https://www.nowcoder.com/questionTerminal/abc3fe2ce8e146608e868a70efebf62e
来源：牛客网
最佳答案：从左下角或者右上角开始搜寻

思路：首先我们选择从左下角开始搜寻，

(为什么不从左上角开始搜寻，左上角向右和向下都是递增，
那么对于一个点，对于向右和向下会产生一个岔路；
如果我们选择从左下脚开始搜寻的话，如果大于就向右，如果小于就向下)。

所以可以从两个边角作为起点开始搜寻，一个是左下角，一个是右上角
'''
#从左下角开始搜寻
def Find_fromleftdown(target, array):
    # write code here
    rows = len(array) - 1
    cols = len(array[0]) - 1
    i = rows
    j = 0
    while j <= cols and i >= 0:
        if target < array[i][j]:
            i -= 1
        elif target > array[i][j]:
            j += 1
        else:
            return True
    return False
#从右上角开始搜寻
def Find_fromrightup(target, array):
    # write code here
    rows = len(array) - 1
    cols = len(array[0]) - 1
    i = 0
    j = cols
    while j >= 0 and i <= rows:
        if target < array[i][j]:
            j -= 1
        elif target > array[i][j]:
            i += 1
        else:
            return True
    return False


def Find(target, array):
    # write code here
    raws = len(array)
    columns = len(array[0])
    for i in range(raws):
        for j in range(columns):
            number = array[i][j]
            if target == number:
                return 'true'
            elif target > number:
                continue
            elif target < number:
                j = j - 1
                for k in range(i, raws):
                    number = array[k][j]
                    if target == number:
                        return 'true'
                    elif target > number:
                        continue
                    elif target < number:
                        return 'false'


target = 5
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]

# print(Find(target,array))
