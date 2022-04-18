s=list(input())
t=list(input())

for i in range(len(s)):
    if len(s)-i<len(t):
        print("No")
        exit()
    if s[i]==t[0]:
        flg=True
        for j in range(len(t)):
            if s[i+j]!=t[j]:
              flg=False  
        if flg==True:
            print("Yes")
            exit()
print("No")
