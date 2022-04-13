a,b,c=map(int,input().split())

ans=0
if not a==b:
    ans+=1
if not a==c:
    ans+=1
if not b==c:
    ans+=1
if ans==0:
    ans=1

print(ans)
