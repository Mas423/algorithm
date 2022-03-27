N=int(input())
A_l=list(map(int,input().split()))

for i in range(N+1):
    flg=True
    for A in A_l:
        if A==i:
            flg=False
    if flg==True:
        print(i)
        break
