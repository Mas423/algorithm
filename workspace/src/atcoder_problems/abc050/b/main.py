n=int(input())
t=list(map(int,input().split()))
m=int(input())
p=[0]*m
x=[0]*m
for i in range(m):
    p[i],x[i]=map(int,input().split())

sum=sum(t)

for i in range(m):
    t_=t[p[i]-1]
    print(sum+(x[i]-t_))
