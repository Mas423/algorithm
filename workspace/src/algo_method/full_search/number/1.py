N=int(input())

cnt=0
for num in range(1,N+1):
    if (num%2 and num%3 and num%5):
        cnt+=1
print(cnt)
