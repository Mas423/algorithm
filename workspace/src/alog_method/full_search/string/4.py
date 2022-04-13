n=int(input())
s=list(input())
t=list(input())

cnt=0
for i in range(n):
    if s[i]!=t[i]:
        cnt+=1
print(cnt)
