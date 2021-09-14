a =int(input("1: "))
b = int(input("2: "))
  
  if a == 0:
    print(b)
  elif b == 0:
    print(a)
  # else implícito aqui também
  else:
   Dividendo, Divisor = abs(a), abs(b)

  while True:
    Resto = Dividendo % Divisor
    if Resto == 0:
          print(Divisor)
  # sai da função!
    # else implícito
    Dividendo = Divisor
    Divisor = Resto 