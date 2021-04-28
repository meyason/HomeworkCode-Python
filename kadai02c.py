#二次方程式の解を導出
print("二次方程式ax^2+bx+c=0のa,b,cを入力")

#abcの入力
a = float(input("a>"))
b = float(input("b>"))
c = float(input("c>"))

D = (b**2 - 4*a*c)
abs (D) <= 1e-5
#判別式Dの代入、絶対値による誤差の指定

if a != 0:
    x1 = f"{(-b + D**0.5) / (2*a): .1g}"
    x2 = f"{(-b - D**0.5) / (2*a): .1g}"
#aが0でないときの解をx1,x2とし、有効数字1桁でとる

if (a==0 and b!=0):
    x = -c/b
    print ("a=0より、解は", f"{x: .1g}")
#以下、判別式による判定
elif D == 0:
    print("重解より、解は", x1)
elif D > 0:
    print("解は二つの実数より、", x1, x2)
else:
    print("解は二つの共役複素数より、", x1, x2)