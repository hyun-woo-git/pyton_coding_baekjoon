def counting_sort(arr):
    c_arr = [0]*(max(arr))
    for i in arr:
        c_arr[i-1] += 1
    for i in range(max(arr)):
        c_arr[i] += c_arr[i-1]
    o_arr = [-1]*len(arr)
    for i in arr:
        o_arr[c_arr[i-1] -1] = i
        c_arr[i-1] -= 1
    return o_arr
a=[]
for i in range(int(input())):
    a.append(int(input()))
    
result = counting_sort(a)
print('\n'.join(map(str,result)))