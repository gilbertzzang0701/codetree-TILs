s=0
n=input()
n=int(n)
for i in range(2,n):
    if n%i==0:
        s='C'
        break
    elif n%i==1:
        s='N'
print(s)