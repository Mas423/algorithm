n=int(input())

s=[]
for i in range(n):
    s.append(input())

cnt=0
for string in s:
    flg=True
    l=len(string)
    for i in range(l):
        if string[i]!=string[l-i-1]:
            flg=False
            break
    if flg:
        cnt+=1
print(cnt)
