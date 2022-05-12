l,r=map(int,input().split())

cnt=0
for num in range(l,r+1):
    num_str=str(num)
    flg=True
    if len(num_str)==1:
        cnt+=1
        continue
    for i in range(len(num_str)):
        if (num_str[i]!=num_str[len(num_str)-1-i]):
            flg=False
    if flg:
        cnt+=1

print(cnt)
