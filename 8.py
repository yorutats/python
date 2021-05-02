n=int(input("輸入第一行正整數為:"))
list1=input("第二行中數列中的數字為:").split(" ")
list2=[]

for x in range(0,n):
    a=0
    for y in range(0,n):
        if list1[x]==list1[y]:
            #ex.list1[0]=1
            a+=1
    list2.append(a)
    #or list1+=[a]
    #集合才是會覆蓋相同數字

if max(list2)==1:
    print("每個數字剛好只出現1次")  
else:
    mab=0
    ma=0
    for x in range(0,n):
        if list2[x]>ma:
            ma=list2[x]
            mab=x
    print("最大出現次數的數字為:"+list1[mab])
    print("出現次數為:"+str(ma))
    print(list2)
    
    #for x in range(0,n):
        #list3.append(list1.count(list1[x]))
        #print(list3)
