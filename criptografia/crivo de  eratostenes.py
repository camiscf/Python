def crivo_versão_alfa_sem_print(n):
  """asdasdas"""
  
  # Primeiro vamos criar um dicionário com as chaves de 2 a n, sem informações
  informações = {}
  for chave in range(2,n +1): #+1 para poder chegar até n
    informações[chave] = 'não sei'

  for atual, marcação in informações.items():
    if marcação == 'composto':
      continue
    # else implícito!
    # descobri que atual é primo!
    informações[atual] = 'primo'
    # vamos eliminar os seus múltiplos

    for múltiplo in range(atual + atual, n+1, atual):
      informações[múltiplo] = 'composto'

  lista_de_primos = []
  for atual, marcação in informações.items():
    if marcação == 'primo':
      lista_de_primos.append(atual)

  return lista_de_primos

def crivo_versão_beta_sem_print(n):
  """asdasdas"""
  
  # Primeiro vamos criar um dicionário com as chaves de 2 a n, sem informações
  informações = {}
  for chave in range(2,n +1): #+1 para poder chegar até n
    informações[chave] = 'não sei'

  for atual, marcação in informações.items():
    if marcação == 'composto':
      continue
    # else implícito!
    # descobri que atual é primo!
    if atual*atual > n:
      break
    informações[atual] = 'primo'
    # vamos eliminar os seus múltiplos
    for múltiplo in range(atual*atual, n+1, atual):
      informações[múltiplo] = 'composto'

  lista_de_primos = []
  for atual, marcação in informações.items():
    if marcação != 'composto':
      lista_de_primos.append(atual)

  return lista_de_primos