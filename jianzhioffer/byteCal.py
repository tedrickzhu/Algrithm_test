#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:byteCal.py
#time:2019/3/25 下午4:59

'''
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

解题思路：
由于题目限制，所以不能直接用公式求解，只能考虑使用递归，或者循环累加，
1.需利用逻辑与的短路特性实现递归终止。 2.当n==0时，(n>0)&&((sum+=Sum_Solution(n-1))>0)只执行前面的判断，为false，然后直接返回0；
3.当n>0时，执行sum+=Sum_Solution(n-1)，实现递归计算Sum_Solution(n)。
    public int Sum_Solution(int n) {
        int sum = n;
        boolean ans = (n>0)&&((sum+=Sum_Solution(n-1))>0);
        return sum;
    }

'''
'''
利用Python and 的特性，当and前后均为真的时候，返回后面的值。
'''
def sum0(n):
    return n and n+sum0(n-1)

print(sum0(10))



def Sum_Solution0(count, n):
    # write code here
    count += n
    temp = (n > 0) and ((Sum_Solution0(count,n-1))) > 0
    return count
#输出为10，因为传入的是形参，返回后的count用来比较大小了，并未传回
print(Sum_Solution0(0,10))


