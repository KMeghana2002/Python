l=[5,17,1,7,6,-2,56]
for ind1 in range(1):
    li=ind1
    for ind2 in range(ind1+1,len(l)):
        if l[ind2]<l[li]:
            li=ind2
        l[ind1],l[li]=l[li],l[ind1]
print(l)
