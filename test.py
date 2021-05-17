def merge_sort(list):
    if len(list)<=1:
        return list
    else:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left,right)

def merge(left,right):
    result = []
    i = j =0
    while i<len(left) and j <len(right):
        if left[i]>right[j]:
            result.append(right[j])
            j+=1
        else:
            result.append(left[i])
            i+=1
    if i<len(left):
        result += left[i:len(left)]
    else:
        result += right[j: len(right)]
    return result

a=[]
for _ in range(int(input())):
   a.append(int(input()))

print('\n'.join(list(map(str, merge_sort(a)))))