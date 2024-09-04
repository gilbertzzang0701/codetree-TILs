sum_val=0
arr=list(map(int,input().split()))
for i in range(len(arr)):
    if i>250:
        break
    sum_val+=i
print(sum_val,sum_val/len(arr))