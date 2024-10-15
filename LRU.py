import sys
hit = 0
miss = 0
cont = 0
cont2 = 0
controle = 0
tam = int("\n".join(sys.argv[1])) #dá set no tamanho das pages
lista = [-1] * tam #cria a lista de pages vazias
lista2 = [-1] * (tam-1) #cria a lista de pages vazias
lis = list(map(int,sys.argv[2].split(','))) #cria a lista das paginas dos processos
for i in range(len(lis)):
    print(f'pages: {lis[i]}')
    if lis[i] in lista: #se der hit
        hit = hit + 1
        if lis[i] in lista2:
            if lis[i] == lista2[cont2]:
                if cont2 == tam-2:
                    cont2 = 0
                else:
                    cont2 += 1
        for z in range(tam):
            if lis[i] != lista[z]:
                print(f'[{lista[z]}]')

            else:
                print(f'[{lista[z]}] <- (hit)')

    else: #se der miss
        miss= miss + 1
        # if lis[i] not in lista2:
        #     lista2[cont2] = lis[i]
        #     if cont2 == tam-2:
        #         cont2 = 0
        #     else:
        #         cont2 += 1
        for z in range(tam):
        #     if lis[z] in lista2:
        #        print(f'[{lista[z]}]')
        #     else:
        #        lista[z] = lis[i]
        #        print(f'[{lista[z]}] <- (miss)')
            # print(lis[z], lista2)
            if lis[i] not in lista2 and controle == 0:
                lista[z] = lis[i]
                print(f'[{lista[z]}] <- (miss)')
                controle += 1
            else:
                print(f'[{lista[z]}]')
        
        if lis[i] not in lista2:
           lista2[cont2] = lis[i]
           if cont2 == tam-2:
               cont2 = 0
           else:
               cont2 += 1
        controle = 0
print(f'Hit rate: {hit}/{len(lis)}')
print(f'Miss rate: {miss}/{len(lis)}')