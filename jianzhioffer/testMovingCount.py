#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:testMovingCount.py
#time:2019/3/21 下午8:37

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here深度优先遍历
        if threshold<0:
            return 0
        i = 0
        j = 0
        visited = [(0, 0)]
        stack = [(0, 0)]
        count = 1
        while len(stack) > 0:
            right = (i, j + 1)
            left = (i, j - 1)
            up = (i - 1, j)
            down = (i + 1, j)
            nextlist = [right, left, up, down]
            for next in nextlist:
                if next not in visited and self.get_ij_sum(next) <= threshold and 0 <= next[0] < rows and 0 <= next[
                    1] < cols:
                    stack.append(next)
                    visited.append(next)
                    print(next)
                    count = count + 1
            newnext = stack.pop()
            i = newnext[0]
            j = newnext[1]
        print(count)
        return count

    def get_ij_sum(self, (chushu_i, chushu_j)):
        sum_r = 0
        sum_c = 0
        while chushu_i > 0:
            sum_r = sum_r + chushu_i % 10
            chushu_i = chushu_i / 10
        while chushu_j > 0:
            sum_c = sum_c + chushu_j % 10
            chushu_j = chushu_j / 10
        return sum_r + sum_c


if __name__ == '__main__':
    sol = Solution()
    sol.movingCount(5,10,10)