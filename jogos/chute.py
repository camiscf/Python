#aqui tem a declaração das coisas
import random

n = 0


#aqui tem o programa 
print('*************************************')
print('******     CHUTE O NÚMERO      ******')
print('*************************************')


x = random.randint(0,50)
continuar = 'S'

n = 1000
while (n != x):
    n = int(input("Chute um número inteiro de 0 a 50: "))
    print("Você errou")
    if (n < x): 
        print('Chute mais alto\n\n')
    else:
        print('Chute mais baixo\n\n')
print('PARABÉNS!')
