def fib(x:int):
    if x==1:
        return 0
    if x==2:
        return 1
    if dp[x]!=0:
        return dp[x]
    else:
        dp[x]=fib(x-1)+fib(x-2)
        return dp[x]

x=int(input())
dp=[]
for i in range(100000):
    dp.append(0)
print(fib(x))