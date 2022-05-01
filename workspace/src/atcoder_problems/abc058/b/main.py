o=list(input())
e=list(input())

sum_len=len(o)+len(e)

ans=[""]*sum_len

for i in range(len(e)):
    ans.append(o[i])
    ans.append(e[i])

if sum_len%2:
    ans.append(o[len(o)-1])

print("".join(ans))
