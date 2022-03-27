N=int(input())
A=list(map(int,input().split()))
max_i=len(A)-1
for i in range(max_i, -1, -1):
    print(A[i])
