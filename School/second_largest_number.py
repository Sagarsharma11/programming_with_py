arr = [12,1,23,43,29,74,9,10,20,31,2,0,74]
n=len(arr)
arr.sort()
largest,second=arr[-1],-1

for i in range(n):
    if(arr[i]>second and arr[i]!=largest):
        second = arr[i]
print(arr)
print(second)