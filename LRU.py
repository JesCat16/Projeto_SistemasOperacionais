import sys

hit = 0 # numero de acertos
miss = 0 # numero de erros
# cont = 0
# cont2 = 0
# controle = 0
# tam = int("\n".join(sys.argv[1])) #dá set no tamanho das pages
# lista = [-1] * tam #cria a lista de pages vazias
# lista2 = [-1] * (tam-1) #cria a lista de pages vazias
# lis = list(map(int,sys.argv[2].split(','))) #cria a lista das paginas dos processos
# for i in range(len(lis)):
#     print(f'pages: {lis[i]}')
#     if lis[i] in lista: #se der hit
#         hit = hit + 1
#         if lis[i] in lista2:
#             if lis[i] == lista2[cont2]:
#                 if cont2 == tam-2:
#                     cont2 = 0
#                 else:
#                     cont2 += 1
#         for z in range(tam):
#             if lis[i] != lista[z]:
#                 print(f'[{lista[z]}]')

#             else:
#                 print(f'[{lista[z]}] <- (hit)')

#     else: #se der miss
#         miss= miss + 1
#         # if lis[i] not in lista2:
#         #     lista2[cont2] = lis[i]
#         #     if cont2 == tam-2:
#         #         cont2 = 0
#         #     else:
#         #         cont2 += 1
#         for z in range(tam):
#         #     if lis[z] in lista2:
#         #        print(f'[{lista[z]}]')
#         #     else:
#         #        lista[z] = lis[i]
#         #        print(f'[{lista[z]}] <- (miss)')
#             # print(lis[z], lista2)
#             if lis[i] not in lista2 and controle == 0:
#                 lista[z] = lis[i]
#                 print(f'[{lista[z]}] <- (miss)')
#                 controle += 1
#             else:
#                 print(f'[{lista[z]}]')
        
#         if lis[i] not in lista2:
#            lista2[cont2] = lis[i]
#            if cont2 == tam-2:
#                cont2 = 0
#            else:
#                cont2 += 1
#         controle = 0
# print(f'Hit rate: {hit}/{len(lis)}')
# print(f'Miss rate: {miss}/{len(lis)}')

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

#LRU
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
            copy = paginas.copy() # faz uma cópia das páginas na memória
            k = p # faz uma cópia da posição atual da lista
            while k >= 0: # itera sobre a lista verificando as páginas acessadas mais recentemente para as mais antigas
                if len(copy) != 1: # previne que a copia não fique vazia
                    if lista[k] in copy: # caso o elemento esteja na memória
                        copy.pop(copy.index(lista[k])) # retira a página da cópia
                k = k - 1
            aux = paginas.index(copy[0]) #pega a primeira página disponível   
        paginas[aux] = lista[p] # substitui a página
        printar(paginas, aux, False) # printa as páginas na tela
print(f'Hit rate = {hit}/{len(lista)}\nMiss rate = {miss}/{len(lista)}')