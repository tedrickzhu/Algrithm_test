#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:mirrorBinTree.py
#time:2019/3/25 下午4:17

# class TreeNode:
#     def __init__(self):
#         self.val = None
#         self.left = None
#         self.right = None

'''
深度遍历互换所有节点的左右子节点
非递归（迭代）实现
'''
def mirrorBinTree(root):

    if root is None:
        return None
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        temp = current.left
        current.left = current.right
        current.right = temp
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return root

'''
递归实现
'''
class Solution:
    def Mirror(self, root):
        # write code here
        if root is None:
            return None
        self.changeChilds(root)
        return root


    def changeChilds(self, current):
        if current is None:
            return None
        temp = current.left
        current.left = current.right
        current.right = temp
        if current.right is not None:
            self.changeChilds(current.right)
        if current.left is not None:
            self.changeChilds(current.left)
