def merge_sort(list):
    if len(list)<=0:
        return list
    else:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(right,left)

def  merge(right,left):
    result =[]
    i = j = 0
    while i<len(right) and j<len(left):
        if right[i]>left[j]:
            result.append(left[j])
            j+=1
        else:
            result.append(right[i])
            i+=1
    if i<len(right):
        result += right[i:len(right)]
    else:
        result += left[j:len(left)]
    
    return result

a=[]
for _ in range(int(input())):
    a.append(int(input()))
for i in merge_sort(a):
    print(i)
