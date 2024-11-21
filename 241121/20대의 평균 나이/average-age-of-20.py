cnt=0
cntcnt=0
while True:
    n=input()
    n=int(n)
    if n<20 or n>=30:
        break
    cnt+=n
    #print(n)
    cntcnt+=1
    #print(cntcnt)
print("%.2f"%(cnt/cntcnt))