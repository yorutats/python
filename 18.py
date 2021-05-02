li={"OO":{"O"},"AO":{"A","O"},"BO":{"B","O"},"ABO":{"A","B"}
    ,"AA":{"A","O"},"AB":{"A","O","AB","B"},"AAB":{"A","B","AB"},
    "BB":{"B","O"},"ABB":{"A","B","AB"},"ABAB":{"A","B","AB"}}
ans=[]
nu=int(input("輸入資料量:"))
for x in range(0,nu):
    lis=input("").split(" ")
    pl=[lis[0],lis[1]]
    pl=sorted(pl)
    p=""
    for x in range(0,2):
        p+=pl[x]

    if lis[2] in li[p]:
        ans+=["YES"]
    else:
        ans+=["IMPOSSIBLE"]

for x in range(0,len(ans)):
    print(ans[x])
