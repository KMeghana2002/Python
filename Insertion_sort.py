l=[19,23,5,24,7]
for ind1 in range(1,len(l)):
    h=ind1
    val=l[h]
    while h>0 and val<l[h-1]:
        l[h]=l[h-1]
        h=h-1
    l[h]=val
print(l)
