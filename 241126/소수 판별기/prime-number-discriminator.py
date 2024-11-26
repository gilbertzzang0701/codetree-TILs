n=input()
n=int(n)
s=0
for i in range(2,n):
    if n%i== 0:
        s='C'
        break
    else:
        s='P'
print(s)
