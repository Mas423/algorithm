# n: 2つの値が決まったらもう1つの値が1通りになるやーつ
# 勘所は良かったが、解けない
# https://drken1215.hatenablog.com/entry/2019/07/06/221600
k,s=map(int,input().split())

cnt=0
for i in range(k+1):
    for j in range(k+1):
        z=s-i-j
        if z>=0 and z<=k:
            cnt+=1
print(cnt)
