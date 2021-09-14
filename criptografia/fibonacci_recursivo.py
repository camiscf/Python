def fibonacci_recursivo (n):
    if n <=1:
        return n
    #else
    return fibonacci_recursivo(n-2) + fibonacci_recursivo(n-1)


def fibonacci_iterativo (n):
    anterior, atual = 0,1
    for i in range(n+1):
        anterior, atual = atual, anterior+atual 
        """ anterior = 0
            atual = 1 
            so q agora 1 vira anterior 
            e agora o atual vai ser a soma = 0+1
            isso vira anterior
            atual vai ser a soma 1+1"""
    return anterior

fibonacci_conhecido = {}
def fibonacci_recursivo_memorizado:
    if n <= 1:
        return n
    if n in fibonacci_conhecido:
        return fibonacci_conhecido[n]
    resultado = fibonacci_recursivo_memorizado(n-2) + fibonacci_recursivo_memorizado (n-1)
    fibonacci_conhecido[n] = resultado

    return resultado