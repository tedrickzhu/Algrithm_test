#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:binTreeDepth.py
#time:2019/3/21 下午9:08

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
对于层数的保存有如下方法：
1，在遍历节点加入队列的时候将节点及其所在的层数组成一个二元组一起存入队列，最后出对列的那个元素一定是最底层的
2，用两个计数器记录每层进入的节点数和弹出的节点数，当进入的节点均弹出后，深度+1
3，每层都使用一个新的队列来存，如果队列空了则深度+1
'''
import Queue
class Solution:
    def TreeDepth(self, pRoot):
    # write code here广度优先遍历，非递归
        if pRoot is None:
            return 0
        que = Queue.Queue()
        que.put(pRoot)
        incount = 1
        outcount = 0
        depth = 0
        while not que.empty():
            current = que.get()
            outcount+=1
            if current.left is not None:
                que.put(current.left)
            if current.right is not None:
                que.put(current.right)
            if outcount == incount:
                depth+=1
                incount = que.qsize()
                outcount = 0
        return depth

'''
方法2：使用递归
如果该树只有一个结点，它的深度为1.如果根节点只有左子树没有右子树，
那么树的深度为左子树的深度加1；同样，如果只有右子树没有左子树，
那么树的深度为右子树的深度加1。如果既有左子树也有右子树，
那该树的深度就是左子树和右子树的最大值加1.
'''
def binTreeDepth(pRoot):
    if pRoot is None:
        return 0
    leftsondepth = binTreeDepth(pRoot.left)
    rightsondepth = binTreeDepth(pRoot.right)
    return max(leftsondepth,rightsondepth)+1

# q = Queue.Queue()
# for i in range(5):
#     q.put(i)
# print(q.get())
# print(q.get())
# print(q.get())


