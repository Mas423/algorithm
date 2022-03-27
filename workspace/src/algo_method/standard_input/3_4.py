N=int(input())
A=list(map(int,input().split()))
for num in A:
    if num%3==0:
        print(num)
        