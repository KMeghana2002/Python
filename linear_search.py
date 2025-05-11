l=[1,2,3,43,-1,78]
val=-1
for ind in range(0,len(l)):
    if val==l[ind]:
        print(ind)
        break
else:
    print(-1)

def lin(l,val):
    for ind in range(len(l)):
        if val==l[ind]:
            return ind
    return -1
l=[1,2,3,43,-1,78]
val=0
print(lin(l,val))
