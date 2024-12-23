arr = list(map(int, input().split()))
a=0
for i in range(len(arr)):
    if arr[i]==0:
        for j in range(1,len(arr)): # 5
            print(arr[i-j],end=' ')
        a=0
        break
    else:
        a=1
if a==1:
    for k in range(len(arr)-1,-1,-1):
        print(arr[k],end=' ')


# for i in range( 4 ,-1)

# 0 1  2  3 4 5
# 3 1 13 5 83 0

#찾는 과정 : 5
# 출력 결과 : 
# 4 3 2 1 0
# 83 5 13 1 3
