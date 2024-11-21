cnt=0
n=input()
n=int(n)
while True:
    cnt+=1
    if n%2==0:
        n=n*3+1
        #print(n)
    elif n%2==1:
        n=n*2+2
        #print(n)
    if n>=1000:
        break
print(cnt)