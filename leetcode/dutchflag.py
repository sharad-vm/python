# Sort colors of a Dutch national flag
flag = [2,2,2,0,0,0,1,1]

def sortFlag(flag):
    low = mid = 0
    high = len(flag)-1

    while mid <= high:
        if flag[mid] == 2:
            flag[mid], flag[high] = flag[high], flag[mid]
            high -= 1
        elif flag[mid] == 0:
            flag[mid], flag[low] = flag[low], flag[mid]
            low += 1
        else:
            mid += 1
    return flag

print(sortFlag(flag))
