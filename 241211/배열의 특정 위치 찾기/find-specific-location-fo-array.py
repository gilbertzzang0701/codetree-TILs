cnt=0
a=0
b=0
arr = list(map(int,input().split()))
for i in range(len(arr)):
    #짝수 값만 합계를 구한다
    if arr[i]%2==0:
        cnt+=arr[i]

    #짝수 위치의 합계를 구한다.
    #if
print(cnt)