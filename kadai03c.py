#sinxのTaylor展開
print("sin(x)をTaylor展開で求める")

degree = int(input("角度x>")) #degreeの入力

import math                   #mathパッケージの読み込み
radian = math.radians(degree) #degreeをradianに変換

num = radian  #分子numの初期化
den = 1       #分母denの初期化
sign = 1      #符号signの初期化
i = 1         #i番目
sinx = radian #sin(x)の初期値

while True:
    par = sign*num / den          #n項目

    num = num * radian**2         #分子の計算
    den = den * (i*2) * (i*2 + 1) #分母の計算
    sign = sign * (-1)            #項の計算

    nextpar = sign*num / den      #n+1項目
    epsilon = abs(par - nextpar)  #項差epsilonの計算

    sinx += nextpar               #sin(x)の計算

    i += 1                        #iを１増やす
    if epsilon<0.001 :
        break                     #無限ループからの脱出

print("sin(x)は",sinx)