a,b=map(int,input("輸入月租費型式及通話時間為:").split(","))
#input().split()可有兩個輸入欄
def m(a,b):
    if a == 186:
        b*=0.09
        if a>=b:
            m=("通話費為:%d"%a)
            return m
        elif b/a<=1:
            b*=0.9
            m=("通話費為:%d"%(round(b,0)))
            return m
        else:
            b*=0.8
            m=("通話費為:%d"%(round(b,0)))
            return m
    if a == 386:
        b*=0.08
        if a>=b:
            m=("通話費為:%d"%a)
            return m
        elif b/a<=1:
            b*=0.8
            m=("通話費為:%d"%(round(b,0)))
            return m
        else:
            b*=0.7
            m=("通話費為:%d"%(round(b,0)))
            return m
    if a == 586:
        b*=0.07
        if a>=b:
            m=("通話費為:%d"%a)
            return m
        elif b/a<=1:
            b*=0.7
            m=("通話費為:%d"%(round(b,0)))
            return m
        else:
            b*=0.6
            m=("通話費為:%d"%(round(b,0)))
            return m
    if a == 986:
        b*=0.06
        if a>=b:
            m=("通話費為:%d"%a)
            return m
        elif b/a<=1:
            b*=0.6
            m=("通話費為:%d"%(round(b,0)))
            return m
        else:
            b*=0.5
            m=("通話費為:%d"%(round(b,0)))
            return m
print(m(a,b))
