N=int(input())
A=list(map(int,input().split()))

max_idx=0
for i in range(1,len(A)):
    if A[i] > A[max_idx]:
        max_idx=i
print(max_idx)
