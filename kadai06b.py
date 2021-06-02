#二つの数値リストを連結して和リストと積リストを作成
a = list(map(int, input("複数の整数の数値をスペース区切りで入力>").split()))
b = list(map(int, input("複数の整数の数値をスペース区切りで入力>").split()))

c = a + b   #リストを連結

i_dict = {} #頻度の辞書を作成
for i in c:
    if i not in i_dict: 
        i_dict[i] = 1    #keyがなかったとき    
    else:
        i_dict[i] += 1   #keyがあったとき 

m_list = [] #積リストの作成
for k, v in list(i_dict.items()):
    if v >= 2: 
        m_list.append(k) #辞書の値>=2の時リストにkeyを格納


print(i_dict)
print(list(i_dict))
print(m_list)


#集合setを使ったとき
print(list(set(a) | set(b)))
print(list(set(a) & set(b)))