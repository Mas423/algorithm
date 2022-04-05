n=int(input())
ans=0
int_arr=list(map(int,input().split()))
i=0
flg=True
while flg:
    for i, a in enumerate(int_arr):
        if a%2:
            flg=False
            break
        int_arr[i] = a//2
        i+=1
    if i == len(int_arr):
        ans+=1
print(ans)
