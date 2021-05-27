#パスカルの三角形を組み合わせの漸化式を利用して求める
n = int(input("正の整数nを入力>"))

pasc = []                    #パスカルの三角形のリスト
comb = []                    #pascに格納する組み合わせのリスト

for x in range(n+1):
    comb = []                #処理するたびに組み合わせのリストを初期化
    a = 0
    b = 0
    c = 0
    
    for k in range(x+1):
        
        if x-1 >= 0:
            a = x-1
        if k-1 >= 0:
            b = k-1
        if k >= 0:
            c = k             #a,b,cが負になると0になるよう処理
        
        if k == 0 or k == x: 
            comb_add = 1      #comb(n,k)でk=0またはnの時は１
        else:
            comb_add = pasc[a][b] + pasc[a][c]
        
        comb.append(comb_add) #組み合わせのリストを作成
    pasc.append(comb)         #パスカルの三角形のリストに格納

print(pasc)