sum=0
q=0
arr = list(map(float,input().split()))
for i in range(len(arr)):
        sum+=arr[i]
        q+=1
print(sum/q)