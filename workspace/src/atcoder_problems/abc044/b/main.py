import collections

w=input()
no="No"
yes="Yes"
c=collections.Counter(w)

for x in c.values():
    if x%2:
        print(no)
        exit()
print(yes)
