N=int(input())
A=list(map(int,input().split()))

max=-100
for num in A:
    if num > max:
        max=num
print(max)
