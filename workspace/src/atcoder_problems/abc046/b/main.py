from tkinter import N

# n: なんとなくの解法は気づけた
n,k=map(int,input().split())

if n==1:
    print(k)
    exit()

sum=k*(k-1)**(n-1)

print(sum)
