l=[87,45,34,12,6,7,9]
for ind1 in range(len(l)-1,0,-1):
    for ind2 in range(ind1):
        if l[ind2]>l[ind2+1]:
            l[ind2],l[ind2+1]=l[ind2+1],l[ind2]
            
print(l)

def bubble(l):
    for ind1 in range(len(l)-1,0,-1):
        for ind2 in range(ind1):
            if l[ind2]>l[ind2+1]:
                l[ind2],l[ind2+1]=l[ind2+1],l[ind2]
print(l)
