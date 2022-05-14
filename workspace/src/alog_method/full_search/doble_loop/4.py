s=input()

l=[]

for i in s:
    flg=True
    for j in range(len(l)):
        if i==l[j]:
            flg=False
    if flg:
        l.append(i)
print(len(l))
