N=int(input())
A_l=list(map(int,input().split()))

sum=1
for A in A_l:
    sum*=A
print(sum)
