#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:subsets.py
#time:2019/3/26 下午3:10
#!/usr/bin/env python3
"""

"""

def PowerSetsBinary(items):
    #generate all combination of N items
    N = len(items)
    #enumerate the 2**N possible combinations
    set_all=[]
    for i in range(2**N):
        #print('i=',i)
        #print('__'*10)
        combo = []
        for j in range(N):
            #print('j=',j)
            #test jth bit of integer i
            if(i >> j ) % 2 == 1:
                print('i=',i,'j=',j)
                combo.append(items[j])
                #print(combo)
        #yield combo
        #print(combo)
        set_all.append(combo)
    return set_all

a=list(range(5))


out= PowerSetsBinary(a)

print(out)