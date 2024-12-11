n=input()
n=int(n)
print(' '.join('*' for _ in range(n)))
for i in range(1, n):
    print(' ' * (2 * (i - 1)) + '*')
