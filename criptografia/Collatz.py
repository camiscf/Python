def Collatz(n):
    if n <= 1:
        return 1
    #else implicito
    #a partir daqui, n >=2
    
    if n%2 == 0:
        return Collatz(n//2)
    #else implicito
    #a partir daqui n é impar
    return Collatz(3*n+1)

def Collatz_passos(n):

  """Quantos passos há na sequência de Collatz começando em n até chegar em 1"""

  if n <= 1:
    return 0
  if n %2 == 0:
    return Collatz_passos(n//2) + 1
  return Collatz_passos(3*n + 1) + 1  

for n in range(50):
  print(f"Collatz({n}) é calculado em {Collatz_passos(n)} passos")

def camadas_Collatz(n):
  "Recebe n e retorna a cebola de todos os Collatz(m) para m <= n"
  cebola = {} # chave é o número da camada, sendo 0 a mais interna
              # conteúdo é a lista dos Collatz(m) daquela camada
  for m in range(n +1): # +1 é pra chegar no n
    camada = Collatz_passos(m)
    if camada not in cebola: 
      # inicializamos a camada com [m]
      cebola[camada] = [m]
    else:
      # camada já tem outros valores, vamos apenas adicionar m
      cebola[camada].append(m)
  return cebola