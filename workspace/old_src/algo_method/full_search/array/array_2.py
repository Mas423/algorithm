N,V=map(int,input().split())
A=list(map(int,input().split()))

ans=0
for num in A:
    if V == num:
        ans+=1
print(ans)
