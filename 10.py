x=input("輸入 N 及 M 為:").split(" ")
target=[]
for q in range(0,int(x[0])):
    #x=2 3 x[0]=2
    li=input("輸入矩陣第"+str(q+1)+"列為:").split(" ")
    target+=[li]
for q in range(0,int(x[1])):
    print("輸出矩陣第"+str(q+1)+"列為:",end=" ")
    for w in range(0,int(x[0])):
        print(target[w][q],end=" ")
    print("")
    
