sum=0
sum_val=0
arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i]==0:
        break
    sum+=arr[i]
    sum_val+=1
print(sum,sum/sum_val)