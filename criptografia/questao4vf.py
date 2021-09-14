def compostos (qntd_numeros):
    altamente_composto = []
    maior_qntd_divisores = 0

    for i in range(1, qntd_numeros+1):
        qntd_divisores = 0
        for j in range(1, qntd_numeros+1):
            if i % j == 0:
                qntd_divisores += 1
        if maior_qntd_divisores < qntd_divisores:
            altamente_composto.append(i)
            maior_qntd_divisores = qntd_divisores

    return(altamente_composto)