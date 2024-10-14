# precisa receber espaços das pages e a lista de valores separados por vírgula OK, uso de sys
# Precisa criar os espaços de acordo com os espaços das pages dados pelo usuário 
# e colocar todos os valores como -1 OK, uso do split
# Precisa separar os números que estão separados por vírugula em uma lista ok, .split
import sys
hit = 0
miss = 0
tam = int("\n".join(sys.argv[1])) #dá set no tamanho das pages
lista = [-1] * tam #cria a lista de pages vazias
lis = list(map(int,sys.argv[2].split(','))) #cria a lista das paginas dos processos
#print(tam, lis, lista)
for i in range(len(lis)):
    print(f'pages: {lis[i]}')
    if i in lista:
        hit = hit + 1
    else:
        miss= miss + 1
print(f'Hit rate: {hit}/{len(lis)}')
print(f'Miss rate: {miss}/{len(lis)}')