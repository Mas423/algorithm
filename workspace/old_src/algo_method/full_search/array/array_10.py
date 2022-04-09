N=int(input())
A=list(map(int,input().split()))

# 配列の初期化数をNにしてREを連発してしまった
# NG: l=[0]*N
l=[0]*9
for num in A:
    l[num-1]+=1

max=0
for i in range(9):
    if l[i] > l[max]:
        max=i

ans = max+1
print(ans)

