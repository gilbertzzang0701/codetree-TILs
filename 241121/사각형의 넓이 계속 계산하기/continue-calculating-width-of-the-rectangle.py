box=0
while True:
    n=input()
    a,b,c=n.split()
    a=int(a)
    b=int(b)
    box=a*b
    print(box)
    if c=='C':
        break
#print(box)