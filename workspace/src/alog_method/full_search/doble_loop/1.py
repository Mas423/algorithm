n=int(input())
A=list(map(int,input().split()))

ans=0
for a in A:
    is_prime=True
    if a==1:
        is_prime=False
    for j in range(2,a):
        if a%j==0:
            is_prime=False
            break
    if is_prime:
        ans+=1
print(ans)
