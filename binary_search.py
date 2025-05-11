l=[-4,-1,1,5,22,67,90]
user=91
low=0
high=len(l)-1
while low<=high:
    mid=(low+high)//2
    if l[mid]>user:
        high=mid-1
    elif l[mid]<user:
        low=mid+1
    elif l[mid]==user:
        print(mid)
        break
else:
    print(-1)
    
def bin(l,user,low,high):
    while low<=high:
        mid=(low+high)//2
        if l[mid]>user:
            high=mid-1
        elif l[mid]<user:
            low=mid+1
        elif l[mid]==user:
            return mid
    return -1
l=[-4,-1,1,5,22,67,90]
user=-4
low=0
high=len(l)-1
print(bin(l,user,low,high))
