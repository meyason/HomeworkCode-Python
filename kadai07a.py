#ベクトルの内積を求める
def naiseki(a, b):
    ans = 0
    for xi, yi in zip(a, b):
        ans += xi * yi #内積の導出
    return ans

a = [2, 1]
b = [1, 3] 
print(naiseki(a, b))