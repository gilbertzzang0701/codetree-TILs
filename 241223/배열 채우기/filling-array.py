#arr = list(map(int, input().split()))
#a=0
#for i in range(len(arr)):
#    if arr[i]==0:
#        for j in range(1,len(arr)): # 5
#            print(arr[i-j],end=' ')   # i = 5 , j = 0 -> 5 -> 4
#        break
#    else:a==1
#if a==1:
#    print()



# for i in range( 4 ,-1)

# 0 1  2  3 4 5
# 3 1 13 5 83 0

#찾는 과정 : 5
# 출력 결과 : 
# 4 3 2 1 0
# 83 5 13 1 3





arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        for j in range(i - 1, -1, -1):
            print(arr[j], end=' ')
        break