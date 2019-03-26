#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:twostacks2sque.py
#time:2019/3/25 下午5:50

'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型

思路：
为保持顺序一直，所有数据在进行中转的时候必须保持与入栈时的状态一致，
所以，栈中留存的数据需保持在其中一个固定的栈中，另一个栈在出栈的时候才作为中转使用
每新入栈一个数据，加入到原有数据的栈顶，栈1的栈顶。
出栈时，将所有数据转入栈2，此刻栈1栈顶的数据在栈2栈底，栈1栈底的数据在栈2的栈顶
弹出栈2的栈顶元素，即为最早入栈的元素
'''
class Solution:
    def __init__(self):
        self.stackin = []
        self.stackout = []

    def push(self, node):
        # write code here
        self.stackin.append(node)

    def pop(self):
        #有数据可出栈
        if len(self.stackin)>0:
            #中转栈空置可用
            if len(self.stackout)==0:
                while len(self.stackin)>0:
                    self.stackout.append(self.stackin.pop())
                output = self.stackout.pop()
                while len(self.stackout)>0:
                    self.stackin.append(self.stackout.pop())
                return output
            else:
                return -1
        else:
            return -1
