w,a,b=map(int,input().split())

if a>b+w:
    print(a-(b+w))
    exit()
if b>a+w:
    print(b-(a+w))
    exit()
print(0)
