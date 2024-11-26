s=0
for i in range(5):
    n=input()
    n=int(n)
    if n%3==0:
        s=1
    else:
        s=0
        break
if s==1:
    print(1)
else:
    print(0)
