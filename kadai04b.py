#数値リストの分散を算出
x_list = list(map(float, input("複数の数値をスペース区切りで入力>").split()))
print("入力:", x_list)
n = len(x_list)

#変数の初期化
ave = 0  #平均の変数ave
var = 0  #分散の変数var
sum1 = 0 #aveの分子
sum2 = 0 #varの第一項分子

for x in x_list:
    sum1 += x
    sum2 += x**2

ave = sum1/n          #平均の計算
var = sum2/n - ave**2 #分散の計算

print("分散:", var)