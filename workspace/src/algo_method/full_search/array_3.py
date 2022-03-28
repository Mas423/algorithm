n=int,input().split()
a=list(map(int,input().split()))

ans=0
for num in a:
    if 0 < num:
        ans+=1
print(ans)
