num=list(input("輸入一整數:"))
ma=0
for x in range(0,len(num)):
    stap=""
    #將數字分別加入stap(如72="7,2,72")
    for y in range(x,len(num)):
        stap+=num[y]
        ck=True
        for z in range(2,int(stap)):
            if int(stap)%z==0:
                ck=False
                break
        if ck:
            if int(stap)>ma:
                ma=int(stap)

if ma==0:
    print("子字串中最大的質數值為:No prime found")
else:
    print("子字串中最大的質數值為:"+str(ma))
