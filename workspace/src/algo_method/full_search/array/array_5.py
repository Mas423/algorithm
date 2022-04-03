N=int(input())
A=list(map(int,input().split()))

count=0
for i in range(len(A)):
    if i <= N-1 and i <= N-1:
        if i > 0 and A[i] > A[i-1]:
            count+=1
print(count)
