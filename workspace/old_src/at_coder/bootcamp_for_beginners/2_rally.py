# NG
# 全探索でいけると計算量で判断する
N=int(input())
X=list((map(int,input().split())))

ans=1001001001
for p in range(1,100):
    now=0
    for i in range(N):
        now += (X[i]-p)**2
    ans=min(ans, now)

print(ans)
