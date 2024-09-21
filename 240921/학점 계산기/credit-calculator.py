sum=0
n=input()
n=int(n)
arr = list(map(float,input().split()))
for i in range(len(arr)):
    sum+=arr[i]  
if sum/n>=4.0:
        print('%.1f' %(sum/n))
        print('Perfect')
if sum/n>=3.0:
        print('%.1f' %(sum/n))
        print('Good')
if sum/n<3.0:
        print('%.1f' %(sum/n))
        print('Poor')