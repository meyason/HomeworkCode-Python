#最大値の判定
x = int(input("xを入力>"))
y = int(input("yを入力>"))
z = int(input("zを入力>"))      #3つの整数の入力

if (x>=y and x>=z):            #xが最大の場合
    print("最大値は>", x)
elif (y>=z):                   #xが最大でなく、yが最大の場合
    print("最大値は>", y)
else :                         #xもyも最大でない、つまりzが最大
    print("最大値は>", z)
#同じ値があっても最大値は変わらない    