# 費氏數列 Fibonacci
# 第0項是0, 第1項是1
# 第n項是(n-1)和(n-2)的總和
# example : 0 ,1 ,1 ,2 ,3 ,5 ,8 ,13 ,21 ...

def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(40))