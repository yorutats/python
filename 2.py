n=int(input())
def m():
    if n<=120:
        s=n*2.1
        w=n*2.1
        return s,w
    elif n<=330:
        s=(n-120)*2.1+252
        w=(n-120)*2.68+252
        return s,w
    elif n<=500:
        s=(n-330)*4.39+886.2
        w=(n-330)*3.61+814.8
        return s,w
    elif n<=700:
        s=(n-500)*4.97+1632.5
        #(500-330)*4.39+886.2
        w=(n-500)*4.01+1428.5
        return s,w
    else:
        s=(n-700)*5.63+2626.5
        w=(n-700)*4.5+2230.5
        return s,w
s,w=m()
print("Summer months:%2.2f\nNon-Summer months:%2.2f"%(s,w))
