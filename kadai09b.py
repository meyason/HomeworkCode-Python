#二分点による二次関数f(x)の解の絞り込み
def fsqrt(x, n): 
    return x**2-n

def nibun(a, b, e, f, n):
    while True:
        c = (a + b)/2
        if abs(f(c, n)) < e: #誤差がe以下になったら終了
            break
        elif f(c, n) > 0:
            b = c
            continue
        elif f(c, n) < 0:
            a = c
            continue
    ans = c
    return ans

print(nibun(a=0, b=2, e=0.1, f=fsqrt, n=2))