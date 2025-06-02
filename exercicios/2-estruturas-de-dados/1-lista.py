# Crie uma lista apenas com elementos numéricos
numerico = [1,2,3,4]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
mista = ['python',2,[5,6,7],'ola mundo',3,90,[2,3]]
print
# Imprima na tela apenas os 5 primeiros elementos da lista
print(mista[0:4])
# Crie um slice na lista para que imprima na tela os elementos de índice par
print(mista[0:len(mista):2])
# Remova da lista o último item
mista.remove(mista[6])
print(mista)
# Insira na lista um novo item
mista.append('URT7')
# Remova da lista um item específico
mista.remove('python')
print(mista)