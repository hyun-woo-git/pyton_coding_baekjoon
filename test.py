def counting_sort(arr, max):
    c_arr = [0]*(max+1)
    for i in arr:
        c_arr[i] += 1
    for i in range(max):
        c_arr[i+1] += c_arr[i]
    o_arr = [-1]*len(arr)
    for i in arr:
        o_arr[c_arr[i] -1] = i
        c_arr[i] -= 1
    return o_arr
a=[]
for i in range(int(input())):
    a.append(int(input()))
    
result = counting_sort(a,max(a))
print('\n'.join(map(str,result)))