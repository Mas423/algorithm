a=list(input())
b=list(input())
c=list(input())

next=a.pop()
w=""
while True:
    if (next=="a"):
        if len(a)==0:
            w="A"
            break
        else:
            next=a.pop()
    elif (next=="b"):
        if len(b)==0:
            w="B"
            break
        else:
            next=b.pop()
    elif (next=="c"):
        if len(c)==0:
            w="C"
            break
        else:
            next=c.pop()
print(w)
