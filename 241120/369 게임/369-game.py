n=input()
n=int(n)
for i in range(1,n+1):
    #
    if i%3==1 or '3' in str(i) or '6' in str(i) or '9' in str(i):
        print(0)
    else:
        print(i)