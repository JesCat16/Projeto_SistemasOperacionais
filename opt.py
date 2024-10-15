import sys

hit = 0
miss = 0
paginas = [-1] * int(sys.argv[1])
lista = list(map(int, sys.argv[2].split(',')))
def printar(paginas, pos, isHit):
    if isHit:
        s = 'hit'
    else:
        s = 'miss'
    for z in range(len(paginas)):
        if z == pos:
            print(f'[{paginas[z]}] <- ({s})')
        else:
             print(f'[{paginas[z]}]')

#OPT
for p in lista:
    print(f"page: {p}")
    if p in paginas:
        hit += 1
        a = paginas.index(p)
        printar(paginas, a, True)
    else:
        miss += 1
        if -1 in paginas:
            aux = paginas.index(-1)
        else:
            copy = paginas.copy()
            k = lista.index(p)
            while k < len(lista):
                if len(copy) != 1:
                    if lista[k] in copy:
                        copy.pop(copy.index(lista[k]))
                k += 1
            aux = paginas.index(copy[0])    
        printar(paginas, aux, False)
        paginas[aux] = p