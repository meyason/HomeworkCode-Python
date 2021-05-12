#入力値のGCMを導出
print("2つの正の整数n,mの最大公約数を導出")
n = int(input("n>"))
m = int(input("m>")) #n,mの入力

while True:
    
    r = n%m 
    
    n = m
    m = r     #n,mの更新

    if r ==0:
        break #無限ループからの脱出

print("n,mの最大公約数は", n)