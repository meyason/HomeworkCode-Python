#英字-整数のリストから英字:整数リストの辞書を作成し、英字ごとの和を算出
alphabet_i_list = ["A-3", "B-1", "C-2", "B-5", "C-6", "B-4"]

alphabet_i_dict = {}    #英字-整数リストの辞書を作成
i_list = []             #整数リストを作成

for x in alphabet_i_list:
    a, i = x.split("-") #文字列を-で分割
    i = int(i)          #文字列から整数に変換
    
    if a not in alphabet_i_dict:    #keyがなかったとき
        i_list = [i]                #整数リストにiを格納
        alphabet_i_dict[a] = i_list #辞書にkeyとvalueを作成
    else:                              #keyがあったとき
        i_list = alphabet_i_dict[a]    #辞書に既にあるkey:aの整数リストを取得
        i_list.append(i)               #整数リストにiを格納
        alphabet_i_dict[a] = i_list    #辞書のkey:aに値を戻す

print(alphabet_i_dict)

for k in alphabet_i_dict:
    s = 0                              #英字ごとの合計を変数sとする
    for v in alphabet_i_dict[k]:
        s +=v
    print(k, s)