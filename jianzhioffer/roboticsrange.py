#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:roboticsrange.py
#time:2019/3/21 下午2:35

# 深度优先遍历
def movingCount000(threshold, rows, cols):

    i = 0
    j = 0
    visited = [(0,0)]
    stack = [(0,0)]
    count = 1
    while len(stack)>0:
        right = (i,j + 1)
        left = (i,j - 1)
        up = (i - 1,j)
        down = (i +1,j)
        nextlist = [right,left,up,down]
        for next in nextlist:
            if next not in visited and get_ij_sum(next)<threshold and 0 <= next[0] < rows and 0 <= next[1]<cols:
                stack.append(next)
                visited.append(next)
                count = count + 1
        newnext = stack.pop()
        i = newnext[0]
        j = newnext[1]
    return count

def get_ij_sum((chushu_i,chushu_j)):
    sum_r = 0
    sum_c = 0
    while chushu_i > 0:
        sum_r = sum_r + chushu_i % 10
        chushu_i = chushu_i / 10
    while chushu_j > 0:
        sum_c = sum_c + chushu_j % 10
        chushu_j = chushu_j / 10
    return sum_r+sum_c

'''

利用一个矩阵来同时存储该点是否可达，是否读过，采用深度优先递归遍历，同时往四个方向查找
'''
def movingCount(self, threshold, rows, cols):
    # write code here
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    def block(r,c):
        s = sum(map(int,str(r)+str(c)))
        return s>threshold
    class Context:
        acc = 0
    def traverse(r,c):
        if not (0<=r<rows and 0<=c<cols): return
        if board[r][c]!=0: return
        if board[r][c]==-1 or block(r,c):
            board[r][c]=-1
            return
        board[r][c] = 1
        Context.acc+=1
        traverse(r+1,c)
        traverse(r-1,c)
        traverse(r,c+1)
        traverse(r,c-1)
    traverse(0,0)
    return Context.acc

#错误思路：误以为只有所有可达的点都在左上角，
# 事实上，在左上角可达的部分并不是一个完整的部分，其间的某些部分可能不可达
def movingCount(threshold,rows,cols):
    i = 0
    j = 0
    count = 0
    while i < rows and j < cols:
        sumij = get_ij_sum(i,j)
        if sumij <= threshold:
            print(i, j)
            count = count+1
            j = j+1
        if sumij > threshold or j>=cols:
            i = i+1
            j = 0
    return count




print(movingCount000(15,20,20))


# i = 12
# j = 13
#
# print(get_ij_sum(i,j))
# print(i,j)
#
# stack = [(0,0),(0,1)]
# print(stack,type(stack),(0,0)in stack)
# visited = set((0,0),(0,1))
# print(type(visited),visited,(0,0) in visited)