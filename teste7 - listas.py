names_list = ["verde", "amarelo", "azul", "branco"]
    #           0         1         2         3
    #          -4        -3        -2        -1

number_list = [1,15,2,20,35,33,5,10]
    #          0,1 ,2,3 ,4 ,5 ,6,7

names_list_tuple = ("verde", "amarelo", "azul", "branco")
        #           0         1         2         3

print("> LISTA ORIGINAL:")
print(f"{names_list} \n\n")

print("> VALOR POR INDICE:")
print(f"{names_list[0]} \n")

print("> INDICE POR VALOR :")
print(f"{names_list.index('verde')} \n")

print("> INDICE DE/ATE:")
print(names_list[0:3])
print(f"{names_list[1:4]} \n")

print("> INDICE APARTIR DE:")
print(names_list[1:])
print(f"{names_list[:3]} \n") # o mesmo que de/ate (considerando :X = 0:X)

print("> INDICE DE TRAZ PRA FRENTE:")
print(f"{names_list[-2]} \n")

print("> INDICE DE TRAZ DE/ATE:")
print(f"{names_list[-3:]} \n")


print("ADICIONANDO - extend(final):")
names_list.extend(["preto"]) #cada item a ser adicionado, é separado por "[],"(colchetes)
print(f"{names_list} \n")

print("ADICIONANDO - append(final):")
names_list.append("vermelho") #cada item a ser adicionado é separado por uma ","(vírgula)
print(f"{names_list} \n")

print("ADICIONANDO - insert(posicao selecionada):")
names_list.insert(1,"roxo") #item adicionado, assumindo a posição daquele item mas não substituindo-o
print(f"{names_list} \n")

print("REMOVENDO - pop(remove ultima posicao):")
names_list.pop() #item removido, remove último item da lista
print(f"{names_list} \n")

print("REMOVENDO - remove(remove item por valor):")
names_list.remove('preto') #item removido, remove item apartir do valor
print(f"{names_list} \n")

print("CONTAGEM - conta(ocorrências de itens):")#conta qtd vezes que o item existe na lista
names_list.append("amarelo")
print(f"{names_list.count('amarelo')} \n")

# print("REMOVENDO - limpar(limpa lista):")
# names_list.clear() #limpa lista, zerando-a
# print(f"{names_list} \n")

print("ORDENAR - (ordenação ASC):")
names_list.sort()
number_list.sort()
print(f"{names_list}") #ordena lista do menor para o maior
print(f"{number_list} \n") #ordena lista do menor para o maior

print("ORDENAR - (ordenação DESC):")
names_list.reverse()
number_list.reverse()
print(f"{names_list}") #ordena lista do maior para o menor
print(f"{number_list} \n") #ordena lista do maior para o menor

print("COPIA - (mantendo referência de memória):")
names_list2 = names_list
names_list.remove("verde")
print(f"{names_list2}") #tudo que fizer em 'name_list' irá afetar 'name_list2'. Porque ambas compartilham a mesma referência em memória.
print(f"{names_list} \n") #tudo que fizer em 'name_list' irá afetar 'name_list2'. Porque ambas compartilham a mesma referência em memória.


print("COPIA - (nova referência de memória):")
names_list2 = names_list.copy()
names_list.remove("roxo")
print(f"{names_list2}") #tudo que fizer em 'name_list' não irá afetar 'name_list2'. Porque não compartilham a mesma referência em memória.
print(f"{names_list} \n") #tudo que fizer em 'name_list' não irá afetar 'name_list2'. Porque não compartilham a mesma referência em memória.


print("TUPLES - uma lista imutável(Apenas leitura):") #diferentemente da lista, nos tuples você não poderá adicionar, remover itens, somente metódos de leitura
# names_list_tuple.remove("verde")
# names_list_tuple.pop()
# names_list_tuple.insert(1, 'roxo')
# print(f"{names_list_tuple} \n")
print(f"{names_list_tuple[2]} \n")