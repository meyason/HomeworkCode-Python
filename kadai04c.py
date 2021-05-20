#2つの整数n,kの組み合わせを算出
print("2つの正の整数n,k(<=n)を入力")

while True: #入力したnがk未満の値であった時の処理
    n = int(input("n>"))
    k = int(input("k>"))
    if n<k :
        print("再入力")
        continue
    else:
        break #ループから脱出

#変数の初期化
deno = 1 #分母の積項の変数deno
nume = 1 #分子の積項の変数nume

for x in range(k-1, -1, -1):
    deno *= k-x
    nume *= n-x
comb = nume/deno #combの計算
    
print(n,"C",k,":",comb)