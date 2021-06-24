#台形を利用したf(x)= 4/(1+x^2)、0<=x<=1の定積分
def f3(x):
    return 4/(1 + x**2)

def daikei(a, b, n, f):
    d = (b-a)/n
    ans = 0
    x = a
    for i in range(n):
        ans += (f(x) + f(x+d)) * d / 2 #台形の面積公式
        x += d
    return ans

print(daikei(a=0, b=1, n=4, f=f3))