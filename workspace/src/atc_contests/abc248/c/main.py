n,m,k=map(int,input().split())

cnt=0
for i in range(1,k+1):
    for j in range(1,(k+1-i)):
        cnt+=1
print(cnt)
