x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

ans_x=0
if x1 == x2:
    ans_x=x3
if x2==x3:
    ans_x=x1
if x3==x1:
    ans_x=x2

ans_y=0
if y1 == y2:
    ans_y=y3
if y2==y3:
    ans_y=y1
if y3==y1:
    ans_y=y2


print(ans_x,ans_y)
