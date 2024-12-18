a=0
arr = list(map(int, input().split()))
for i in range(len(arr)):
    a+=arr[i]
    if arr[i]==0:
        break
print(a)