def hanoi(disco, ori, dest, aux):
    if disco == 1:
        print('Mova o disco {} da torre {} para torre {}'.format(disco,ori, dest))
        return
    else:
     # 1. Resolve a torre de Hanoi para n-1 discos, movendo para o disco auxiliar:
    hanoi(disco-1, ori, aux, dest)

    # 2. Move o maior disco para a torre destino:
    print('Move disc {} from tower {} to the tower {}'.format(disco, ori, dest))

    # 3. Resolve a torre de Hanoi para n-1 discos, movendo da torre auxiliar para a destino:
    hanoi(disco - 1, aux, ori, dest)
    
    hanoi(disco - 1, ori, aux, dest)
    print('Mova o disco {} da torre {} oara a torre {}'.format(disco, ori, dest))
    hanoi(disco - 1, aux, dest, ori)