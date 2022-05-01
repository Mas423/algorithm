n,m=map(int,input().split())

a=[0]*n
b=[0]*n
c=[0]*m
d=[0]*m

for i in range(n):
    a[i],b[i]=map(int,input().split())

for j in range(m):
    c[j],d[j]=map(int,input().split())

min_list=[]
for i in range(n):
    index=-1
    min=10000000000
    for j in range(m):
        tmp=abs(a[i]-c[j])+abs(b[i]-d[j])
        if min > tmp:
            min = tmp
            index=j+1
    min_list.append(index)

for num in min_list:
    print(num)
