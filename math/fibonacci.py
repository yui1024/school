#counter = 0
def fib1(n):
    #フィボナッチ数列 n 番目の数字
    global counter
    #counter += 1
    if n in [0, 1]:
        #nが0と1のとき
        #フィボナッチ数列は0番目と1番目は1
        #1,1,2,3,5~のため
        return 1
    return fib1(n - 1) + fib1(n - 2)
n = int(input())
print(fib1(n))

def fib2(n):
    #フィボナッチ数列の表示
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b

print([fib2(i) for i in range(10)])

