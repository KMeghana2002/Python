l=[76,5,34,-1,90,46,46]
for ind1 in range(0,1):
    for ind2 in range(len(l)-1-ind1):
        if l[ind2]<l[ind2+1]:
            l[ind2],l[ind2+1]=l[ind2+1],l[ind2]
print(l[-1])

l=[76,5,34,-1,90,46,46]
for ind1 in range(0,2):
    for ind2 in range(len(l)-1-ind1):
        if l[ind2]<l[ind2+1]:
            l[ind2],l[ind2+1]=l[ind2+1],l[ind2]
print(l[-2])
