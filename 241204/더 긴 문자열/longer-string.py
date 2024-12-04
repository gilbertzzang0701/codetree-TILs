a,b=map(int(input).split())
if len(a)>len(b):
    print(a,len(a))
if len(a)<len(b):
    print(b,len(b))
if len(a)==len(b):
    print('same')