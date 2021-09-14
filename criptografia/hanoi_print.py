def Hanói_print(n, lista_origem, lista_destino, lista_auxiliar):
  if n == 1:
    # caso base, "mova 1 disco da origem pro destino"
    disco = lista_origem.pop()
    lista_destino.append(disco)
    print(f"Situação: {lista_origem}, {lista_destino}, {lista_auxiliar}")
  else:
    Hanói_print(n-1, lista_origem, lista_auxiliar, lista_destino)

    disco = lista_origem.pop()
    lista_destino.append(disco)
    print(f"Situação: {lista_origem}, {lista_destino}, {lista_auxiliar}")

    Hanói_print(n-1, lista_auxiliar, lista_destino, lista_origem)