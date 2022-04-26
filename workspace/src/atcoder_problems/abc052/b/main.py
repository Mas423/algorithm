n=int(input())
s=list(input())

x=0
max=0
for c in s:
    if c=="I":
        x+=1
    if c=="D":
        x-=1
    if x>max:
        max=x
print(max)
