a,b,k=map(int,input().split())

sum=a
cnt=0
while True:
    if (sum >= b):
        print(cnt)
        exit()
    sum*=k
    cnt+=1
