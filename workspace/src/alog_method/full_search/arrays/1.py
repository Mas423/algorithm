n,m=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

cnt=0
for a_num in a:
    for b_num in b:
        if (a_num>b_num):
            cnt+=1
print(cnt)
