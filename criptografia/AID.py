a = int(input("Digite o primeiro natural: "))
b = int(input("Digite o segndo natural: "))

if (b <= 0):
    print("ERRO! B <= 0")
else: 
    q = 0 
    r = a 
    while b <= r:
        print("quociente = {}, resto = {}".format(q,r))
        q += 1
        r -= b
    print('FIM')
