# o: 簡単
a,b,c=map(int,input().split())

yes="Yes"
no="No"
if a+b==c:
    print(yes)
    exit()
if a+c==b:
    print(yes)
    exit()
if b+c==a:
    print(yes)
    exit()
print(no)
