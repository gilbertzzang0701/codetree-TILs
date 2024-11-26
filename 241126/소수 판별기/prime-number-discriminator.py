s=0
n=input()
n=int(n)
while True:
    if n%1==0 and n%n==0:
        s='P'
        break
    else:
        s='C'
        break
print(s)