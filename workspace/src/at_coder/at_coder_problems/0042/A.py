# フラグを使用する意味は皆無だった件
input=list(map(int,input().split()))

yes="YES"
no="NO"

flg=0
input.sort()
if input[0]==5 and input[1]==5 and input[2]==7:
    flg=1

if flg==1:
    print(yes)
else:
    print(no)
