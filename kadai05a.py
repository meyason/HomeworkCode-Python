#整数列1~n-1の長さ２の要素を列挙（同数の組は除く）
n = int(input("整数nを入力>"))

p =[] #空のリストp

for i in range(n):
    for j in range(n):
        if i != j :
            p.append([i, j]) #直積の同じ数字の組を排除

print(p)        