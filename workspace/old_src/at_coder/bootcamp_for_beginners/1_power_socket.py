# 問題文読まなすぎてWA連発
A,B=map(int,input().split())

x=0
while True:
    if A*x+1-x>=B:
        print(x)
        break
    x+=1
