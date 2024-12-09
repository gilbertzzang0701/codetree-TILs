cnt=0
a=input()
b=input()

for i in range(len(a)):
    if a[i] == b:
        cnt+=1
print(cnt)