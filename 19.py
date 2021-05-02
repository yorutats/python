n=int(input("組數為:"))
s=[]
for x in range(0,n):
    n2=input("第"+str(x+1)+"組為:").split(" ")
    s.append(int(n2[0])*250+int(n2[1])*175)
for i in range(0,n):
    print("第"+str(i+1)+"應收費用:"+str(s[i]))
