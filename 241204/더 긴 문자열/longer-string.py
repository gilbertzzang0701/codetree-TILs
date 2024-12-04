n=input()
a,b=n.split()
if len(a)>len(b):
    print(a,len(a))
if len(a)<len(b):
    print(b,len(b))
if len(a)==len(b):
    print('same')