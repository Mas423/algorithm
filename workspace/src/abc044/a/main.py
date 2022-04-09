#!/usr/bin/env pypy3

n=int(input())
k=int(input())
x=int(input())
y=int(input())

sum=0
if n<=k:
    sum+=x*n
else:
    sum+=x*k
    for i in range(n-k):
        sum+=y
print(sum)
