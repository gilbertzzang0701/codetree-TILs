arr = list(map(int, input().split()))
if arr[0]+arr[2]+arr[4]+arr[6]+arr[8]>arr[1]+arr[3]+arr[5]+arr[7]+arr[9]:
    print((arr[0]+arr[2]+arr[4]+arr[6]+arr[8])-(arr[1]+arr[3]+arr[5]+arr[7]+arr[9]))
if arr[0]+arr[2]+arr[4]+arr[6]+arr[8]<arr[1]+arr[3]+arr[5]+arr[7]+arr[9]:
    print((arr[1]+arr[3]+arr[5]+arr[7]+arr[9])-(arr[0]+arr[2]+arr[4]+arr[6]+arr[8]))