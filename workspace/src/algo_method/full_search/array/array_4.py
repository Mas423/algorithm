N,V=map(int,input().split())
A=list(map(int,input().split()))

ans=-1
for i in range(N-1,-1,-1):
    if A[i] == V:
        ans=i
        break
print(ans)
