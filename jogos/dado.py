import random

n = random.randint(1,6)

op = str(input("Você gostaria de jogar o dado? [S/N]   "))
nova = op.upper()
if (nova == 'S'):
    print("O dado deu o número \033[0;31;40m{}\033[m".format(n))
elif (nova == 'N'):
    print("Saindo...")
else:
    print("Opção inválida")
