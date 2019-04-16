# 漸化式の問題　a_n+1 = 1 + 1/(1+a_n)
def zenkashiki(n):
    if n == 0:
        return 1
    else:
        return 1 + 1 / (1 + zenkashiki(n - 1))


n = int(input())
# 小数点以下18桁を表示させる
print(f"{zenkashiki(n):.18e}")
