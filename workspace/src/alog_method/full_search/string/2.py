s=list(input())

n=len(s)

for i in range(n//2):
    if not s[i]==s[(n-1)-i]:
        print("No")
        exit()
print("Yes")
