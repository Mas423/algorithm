s=list(input())

for i in range(len(s)-1):
    if s[i]=="A":
        for j in range(len(s)-1,i,-1):
            if s[j]=="Z":
                print(j-i+1)
                exit()
