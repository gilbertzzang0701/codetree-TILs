cnt=0
s=0
n=input()
n=int(n)
for i in range(1,n+1):
    if n%i== 0:
        s='P'
        continue
    else:
        s='C'
        cnt+=1

if cnt==1:
    print(s)