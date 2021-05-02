n=int(input("請輸入階層值M:"))
a1=s=1
while s<n:
    s*=a1
    a1+=1  
print("超過M為%d的最小階層N值為:%d"%(n,a1-1))
