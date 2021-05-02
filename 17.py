n=input("").split(" ")
a={"A":1,"j":11,"Q":12,"K":13}
b=[]
s=0
for i in range(0,len(n)):
    if n[i] in a:
        b.append(a.get(n[i]))
    else:
        s+=int(n[i])
for i in range(0,len(b)):
    s+=int(b[i])
  

print(s)
