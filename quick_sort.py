def quick(l):
    if len(l)<=1:
        return l
    pivot=l[0]
    left=[ele for ele in l[1:] if ele<pivot]
    right=[ele for ele in l[1:] if ele>=pivot]
    return quick(left)+[pivot]+quick(right)
l=[1,56,78,4,3,345,-5,-4]
print(quick(l))


