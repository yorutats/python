a=input("").split(" ")
c=[]
for i in range(0,int(a[0])):
    b=input("").split(" ")
    c.append(b)
a1=input("").split(" ")
c1=[]
for i in range(0,int(a1[0])):
    b1=input("").split(" ")
    c1.append(b1)
if a[0]!=a1[0]:
    print("兩個矩陣無法相加")
else:
    for i in range(0,int(a[0])):
        for j in range(0,int(a1[0])):
            print(int(c[i][j])+int(c1[i][j]),end=" ")
        print("")
