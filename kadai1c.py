yen =679                     #金額679円

inc_tax = yen + (yen*8) // 100 #税込み価格の変数をinc_taxとし、金額＋税で算出
print(inc_tax)

#以降硬貨の枚数を算出。硬貨の枚数の変数はco〇〇（硬貨の価値）に統一

co500 = inc_tax // 500       #500円玉の枚数
co100 = (inc_tax%500) // 100 #100円玉の枚数
print(co500)
print(co100)

x2 = inc_tax % 100           #税込み価格の１０の位をx2とする
co50 = x2 // 50              #50円玉の枚数
co10 = (x2%50) //10          #10円玉の枚数
print(co50)
print(co10)

x1 = inc_tax % 10            #税込み価格の１の位をx1とする
co5 = x1 // 5                #5円玉の枚数
co1 = x1 % 5                 #1円玉の枚数
print(co5)
print(co1)