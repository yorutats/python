n=list(input("輸入一組四位數字為："))
m=[]
for i in range(0,len(n)):
   a=(int(n[i])+7)%10
   m.append(a)
b=c=0
b=m[0]
m[0]=m[2]
m[2]=b
c=m[1]
m[1]=m[3]
m[3]=c
print("輸出加密後的數字為:",end="")    
for x in range(0,len(m)):
    print(m[x],end="")


