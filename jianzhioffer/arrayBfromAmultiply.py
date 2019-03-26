#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:arrayBfromAmultiply.py
#time:2019/3/25 下午6:24

'''

给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法

'''

class Solution1:
    def multiply(self, A):
        # write code here
        B = []
        for i in range(len(A)):
            bi = 1
            for k in range(len(A)):
                if k == i:
                    continue
                else:
                    bi = bi*A[k]
            B.append(bi)
        return B

class Solution2:
    def multiply(self, A):
        # write code here
        if not A:
            return []
        # 计算前面一部分
        num = len(A)
        B = [None] * num
        B[0] = 1
        for i in range(1, num):
            B[i] = B[i-1] * A[i-1]
        # 计算后面一部分
        # 自下而上
        # 保留上次的计算结果乘本轮新的数,因为只是后半部分进行累加，所以设置一个tmp,能够保留上次结果
        tmp = 1
        for i in range(num-2, -1, -1):
            tmp *= A[i+1]
            B[i] *= tmp
        return B
