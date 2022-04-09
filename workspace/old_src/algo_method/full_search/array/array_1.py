N,V=map(int,input().split())
A=list(map(int,input().split()))

ans="No"
for num in A:
    if V == num:
        ans="Yes"
        break
print(ans)
