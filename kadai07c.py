#ベクトルを回転するrotを求める
def naiseki(a, b):
    ans_nai = 0
    for xi, yi in zip(a, b):
        ans_nai += xi * yi
    return ans_nai

def rotate(a, m):
    #ここからTaylor展開によるsinx, cosxの導出
    import math                   
    radian = math.radians(m) 

    num = radian  
    den = 1       
    sign = 1      
    i = 1         
    sinx = radian 

    while True:
        par = sign*num / den          

        num = num * radian**2         
        den = den * (i*2) * (i*2 + 1) 
        sign = sign * (-1)            

        nextpar = sign*num / den      
        epsilon = abs(par - nextpar)  

        sinx += nextpar               

        i += 1                        
        if epsilon<0.001 :
            break
    cosx = (1 - (sinx)**2)**0.5
    #以下、回転行列の計算処理
    
    x = [cosx, -sinx]
    y = [sinx, cosx]
    r = [x, y]          #回転行列
    x1 = naiseki(a, x)
    y1 = naiseki(a, y)
    ans_rot = [x1, y1]
    return ans_rot

a = [2, 1]
b = [1, 3]
d = rotate(a, 45) # 反時計回り45度
print(d)
print(rotate(d, -45))