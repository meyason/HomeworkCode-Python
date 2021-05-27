#入力した数値を小さいものから順に並べ直す
x_list = list(map(int, input("複数の整数の数値をスペース区切りで入力>").split()))
print("入力:", x_list)
n = len(x_list)

min_i = 0         #インデックス0の数字を初期比較値[min_i]としておく

for x in range(n-1):
    for i in range(x, n):
        if x_list[min_i] > x_list[i]:
           
            min_x = x_list[i]         #比較値[min_i]より小さい値をmin_xとする
            x_list[i] = x_list[min_i] #min_xのインデックスに[min_i]の数字を格納
            x_list[x] = min_x         #最小値をおきたいインデックスに最小値min_xを格納
    
    min_i = x + 1                     #比較したいインデックスの値を次に進める

print(x_list)