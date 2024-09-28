sum=0
arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i]==0:
        break
    sum+=arr[i]
print(sum,sum/i)