#1~nまでの総和を算出
n=int(input("正の整数nを入力>"))

summ = 0                  #1からnまでの和を変数summとする

for x in range(n, 0, -1): #nから始まり-１ずつ加え１で終わる
    summ += x

print(summ)    