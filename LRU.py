import sys

hit = 0
miss = 0
cont = 0
cont2 = 0
controle = 0
tam = int("\n".join(sys.argv[1]))  # pega o tamanho da memória
lista = [-1] * tam  # cria a lista vazia
lista2 = [-1] * tam  # cira uma lista vazia identica para guardar as informações de prioridade
lis = list(map(int, sys.argv[2].split(',')))  # cria uma lista com os números dados

for i in range(len(lis)):
    print(f'Page request: {lis[i]}')
    if lis[i] in lista:  # se for um hit
        hit += 1
        # dá update na lista de prioridade
        for z in range(tam):
            if lista[z] == lis[i]:
                lista2[z] = cont
                cont += 1
        for z in range(tam):
            if lista[z] == lis[i]:
                print(f'[{lista[z]}] <- (hit)')
            else:
                print(f'[{lista[z]}]')
    else:  # se for um miss
        miss += 1
        # encontra qual tem o menor indice na lista 2
        lru_index = lista2.index(min(lista2))
        lista[lru_index] = lis[i]  # troca pelo que foi usado menos recentemente
        lista2[lru_index] = cont
        cont += 1
        for z in range(tam):
            if lista[z] == lis[i]:
                print(f'[{lista[z]}] <- (miss)')
            else:
                print(f'[{lista[z]}]')

print(f'Hit rate: {hit}/{len(lis)}')
print(f'Miss rate: {miss}/{len(lis)}')