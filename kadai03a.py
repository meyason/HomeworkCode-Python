#入力値の平均を導出
print("正の整数を入力")
print("0で入力終了")
print("負の数は再入力")

sum = 0 #合計sumの初期化
i = 1   #i番目
ave = 0 #平均aveの初期化

while True :
    n = int(input(f"{i}:")) #i番目の入力
    if n==0 :
        break               #無限ループからの脱出
    elif n<0 :
        print("再入力")
        continue            #再入力の誘導
    
    sum += n      #sumの計算
    ave = sum / i #平均の計算
    
    i += 1        #iを１増やす

print("入力終了")
print("平均:", ave)