l=[-4,-1,12,45,78,98]
user=90
low=0
high=len(l)-1
while low<=high and l[low]<=user<=l[high]:
    mid=int(low+((high-low)/(l[high]-l[low]))*(user-l[low]))
    if l[mid]>user:
        high=mid-1
    elif l[mid]<user:
        low=mid+1
    elif l[mid]==user:
        print(mid)
        break
else:
    print(-1)
    
def inter(l,low,high,user):
    while low<=high and l[low]<=user<=l[high]:
        mid=int(low+((high-low)/(l[high]-l[low]))*(user-l[low]))
        if l[mid]>user:
            high=mid-1
        elif l[mid]<user:
            low=mid+1
        elif l[mid]==user:
            return mid
    return -1
l=[-4,-1,12,45,78,98]
user=90
low=0
high=len(l)-1
print(inter(l,low,high,user))
