x=int(input("X 軸座標:"))
y=int(input("Y 軸座標:"))
r=x**2+y**2
def xy(x,y):
    if x==0 and y==0:
        xy=("該點位於原點")
        return xy
    if x==0 and y>0:
        xy=("該點位上半平面Y軸上,距離原點為根號%d"%r)
        return xy
    if x==0 and y<0:
        xy=("該點位下半平面Y軸上,距離原點為根號%d"%r)
        return xy
    if x>0 and y==0:
        xy=("該點位右半平面X軸上,距離原點為根號%d"%r)
        return xy
    if x<0 and y==0:
        xy=("該點位左半平面X軸上,距離原點為根號%d"%r) 
        return xy
    if x >0 and y>0:
        xy=("該點位於第一象限,距離原點為根號%d"%r)
        return xy
    if x <0 and y>0:
        xy=("該點位於第二象限,距離原點為根號%d"%r)
        return xy
    if x <0 and y<0:
        xy=("該點位於第三象限,距離原點為根號%d"%r)
        return xy
    if x >0 and y<0:
        xy=("該點位於第四象限,距離原點為根號%d"%r)
        return xy
print(xy(x,y))
