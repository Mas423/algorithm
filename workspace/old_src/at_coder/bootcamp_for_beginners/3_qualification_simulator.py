# 問題文をよく読む系の問題だった
n,a,b=list(map(int,input().split()))
s=input()

sum=0
b_stu=0
yes="Yes"
no="No"
for i in range(n):
    if s[i]=="a":
        if (a+b)>sum:
            sum+=1
            print(yes)
            continue
    elif s[i]=="b":
        b_stu+=1
        if (a+b)>sum and b_stu<=b:
            sum+=1
            print(yes)
            continue
    print(no)

# sumを全体合計とせずに、日本人と海外の方でそれぞれ分けるともっと綺麗
