a,b,c=map(int,input().split())

yes="YES"
no="NO"
if a%2==0 and c%2==1:
    print(no)
    exit()
if a==1:
    print(yes)
    exit()

l=[]
for i in range(1,10**9):
    if a*i in l:
        print(no)
        exit()
    if a*i%b == c:
        print(yes)
        exit()
    l.append(a*i)
