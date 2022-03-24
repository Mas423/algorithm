s = list(input().strip())
n,m = input().split()

ans = []
for i, char in enumerate(s):
    if int(n) == i:
        ans.append(s[int(n)-1])
        continue
    if int(m) == i:
        ans.append(s[int(m)-1])
    ans.append(char)
