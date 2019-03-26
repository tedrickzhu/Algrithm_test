#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:inversePairs.py
#time:2019/3/26 上午10:38

'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。
即输出P%1000000007
'''


# 暴力遍历，O(n^2)
def InversePairs(self, data):
    # write code here
    p = 0
    nums = len(data)
    for i in range(nums - 1):
        for j in range(i + 1, nums):
            if data[i] > data[j]:
                p += 1
    return p % 1000000007


'''
1,将所有数据data复制到一个新的数组copy中
2，将copy中的数据递增排序
3，从copy中递增选取数据x，并且找到x在data中的位置索引index，
    由于x是当前data中最小的元素，所以，该index即表示了x前面有多少元素比他大，即为对于x的逆序对的数量
4，为保证每次从copy中递增取出的元素都是data中最小的，所以，x的获得index之后，即将x从data中移除
5，循环3，4直至data中无数据

复杂度分析：
时间复杂度主要是新数组排序，以及数据的移除。
空间复杂度，新数组占用的空间O(n)
'''
def InversePairs(self, data):
    # write code here
    count = 0
    copy = []
    for i in data:
        copy.append(i)
    copy.sort()

    for i in range(len(copy)):
        count += data.index(copy[i])
        data.remove(copy[i])

    return count % 1000000007

'''
归并排序的思想
'''