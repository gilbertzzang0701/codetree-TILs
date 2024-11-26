s=0
n=input()
n=int(n)
for i in range(1,n+1):
    if n%i==0:
        s='P'
    else:
        s='C'
print(s)