n=input()
a,b,c=n.split()
a=int(a)
b=int(b)
c=int(c)
for i in range(a,b+1):
    if i%c==0:
        print('NO')
        break
    else:
        print('YES')
        break