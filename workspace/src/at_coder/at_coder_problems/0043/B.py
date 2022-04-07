# pythonが便利すぎる
s=input()

l=[]
for x in s:
    if x=="B":
        if len(l)>0:
            l.pop()
            # わざわざ指定しなくていい
            # l.pop(len(l)-1)
    else:
        l.append(x)
print("".join(l))
