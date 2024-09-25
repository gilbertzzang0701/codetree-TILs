arr = list(map(int, input().split()))
zero=0
idx=-1
for i in range(len(arr)):
    if arr[i]==0:
        idx=i
        break
for i in range(len(arr)-1,-1,-1):
    if arr[idx]==0:
        continue
    print(arr[i],end=' ')