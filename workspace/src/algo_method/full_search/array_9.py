# 元の回答
N=int(input())
A=list(map(int,input().split()))

ans=[0]*9
for num in A:
    for i in range(1,10):
        if num == i:
            ans[i-1]+=1
            break
for x in ans:
    print(x)

# 添字と同じことを見逃していた
# 以下線形探索の模範回答
N=int(input())
A=list(map(int,input().split()))

ans=[0]*9
for i in A:
    ans[i-1]+=1
for x in ans:
    print(x)
