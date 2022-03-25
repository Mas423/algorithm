from email.mime.application import MIMEApplication

s=input()
ans=0
for x in s:
    ans+=int(x)
print(ans)

# ---
# countメソッドなるものでもできるみたい
# print(s.count("1"))
