N=int(input())
A=list(map(int,input().split()))

min=100
for num in A:
    if num < min:
        min=num
print(min)
