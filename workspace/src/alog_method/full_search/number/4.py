a,b=map(int,input().split())

min=min(a,b)
ans=1
for i in range(2,min+1):
    if a%i==0 and b%i==0:
        ans=i
print(ans)
