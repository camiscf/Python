def fatoração_ingênua(n):
  """
  Recebe n >= 2 natural e retorna uma lista de primos em ordem não-decrescente
  cujo produto é n
  """
  atual = 2
  dividendo = n
  lista = []

  while True: # laço passo 2 <-> passo 3
    while dividendo % atual == 0: # laço interno do passo 2
      print(f"Descobri que {dividendo} é divisível por {atual}")
      lista.append(atual)
      dividendo //= atual # é o mesmo que dividendo = dividendo // atual
      if dividendo == 1:
        return lista
    print(f"{dividendo} não é divisível por {atual}")
    atual += 1