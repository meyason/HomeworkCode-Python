#ベクトルの長さと余弦cosを求める
def naiseki(a, b):
    ans_nai = 0
    for xi, yi in zip(a, b):
        ans_nai += xi * yi
    return ans_nai

def nagasa(a, b):
    ans_leng = 0
    ans_nagasa = []
    for xi in c:
        ans_leng = naiseki(xi, xi) **0.5 #長さの導出
        ans_nagasa.append(ans_leng)      #ベクトルごとの長さをリストに格納
    return ans_nagasa

def cos(a, b):
    ans_cos = naiseki(a, b)              #分子と分母に分けて考える
    for xi in nagasa(a, b):
        ans_cos *= 1 / xi
    return ans_cos

a = [2, 1]
b = [1, 3]
c = [a, b] #aとbを分けてforで処理するために二つを新たなリストに格納

print(nagasa(a, b))
print(cos(a, b))