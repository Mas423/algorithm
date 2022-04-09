S=input()
N,M=map(int,input().split())
ans_l=[]
for char in S:
    ans_l.append(char)
tmp=ans_l[N-1]
ans_l[N-1]=ans_l[M-1]
ans_l[M-1]=tmp
print("".join(ans_l))
