def mdc_ingênuo(a,b):
  """
  gsdfdsfdsbbdf 
  """
  # se um dos dois for 0, retorne o outro
  if a == 0:
    return b
  #else implícito
  if b == 0:
    return a

  #else implícito
  
  chute_mdc = 1
  atual = 1

  while atual <= min(abs(a), abs(b)): # abs(x) = |x|
    atual += 1
    if a % atual == 0 and b % atual == 0:
      chute_mdc = atual
    
  return chute_mdc