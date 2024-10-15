import sys

hit = 0 # numero de acertos
miss = 0 # numero de erros
paginas = [-1] * int(sys.argv[1]) # número de páginas
lista = list(map(int, sys.argv[2].split(','))) # lista de páginas que vão ser colocadas na memória
def printar(paginas, pos, isHit): # Função para printar as páginas
    if isHit: #verifica se foi um hit ou miss
        s = 'hit'
    else:
        s = 'miss'
    for z in range(len(paginas)): # printa as paginas na tela apontando onde foi o hit ou miss
        if z == pos:
            print(f'[{paginas[z]}] <- ({s})')
        else:
             print(f'[{paginas[z]}]')

#OPT
for p in range(len(lista)): # percorre a lista de paginas
    print(f"page: {lista[p]}") # printa a pagina a ser inserida
    if lista[p] in paginas: # caso a pagina já esteja na memória
        hit += 1
        printar(paginas, p, True)
    else: # caso não esteja
        miss += 1
        if -1 in paginas: # verifica se possui página vazia na memória e preenche a primeira que estiver vazia
            aux = paginas.index(-1)
        else: # caso não tenham páginas vazias
            copy = paginas.copy() # faz uma cópia das páginas da memória
            k = p # faz uma cópia da posição atual da lista
            while k < len(lista): # itera sobre a lista verificando as páginas restantes
                if len(copy) != 1: # previne que a copia não fique vazia
                    if lista[k] in copy: # caso o elemento esteja na memória
                        copy.pop(copy.index(lista[k])) # retira a página da cópia
                k = k + 1
            aux = paginas.index(copy[0]) #pega a primeira página disponível   
        paginas[aux] = lista[p] # substitui a página
        printar(paginas, aux, False) # printa as páginas na tela
print(f'Hit rate = {hit}/{len(lista)}\nMiss rate = {miss}/{len(lista)}')