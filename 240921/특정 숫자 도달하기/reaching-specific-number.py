sum=0
q=0
a = list(map(int, input().split()))
for i in range(len(a)):
    if a[i]>=250:
        break
    sum+=int(a[i])
    q+=1
print(sum,'%.1f' %(sum/q))