n,k=map(int,input().split())

ans=0
for num in range(1,n+1):
    factor=0
    for i in range(1,n+1):
        if num%i==0:
            factor+=1
    if factor==k:
        ans+=1
print(ans)
