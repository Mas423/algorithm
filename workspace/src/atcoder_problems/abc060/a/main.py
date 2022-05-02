a,b,c=input().split()

yes="YES"
no="NO"

if a[-1] == b[0] and b[-1] == c[0]:
    print(yes)
else:
    print(no)
