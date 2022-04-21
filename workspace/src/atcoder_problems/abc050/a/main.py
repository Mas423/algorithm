a,op,b=map(str,input().split())

a_i=int(a)
b_i=int(b)
if op=="+":
    ans=a_i+b_i
if op=="-":
    ans=a_i-b_i

print(ans)
