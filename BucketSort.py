from random import randint
data = [randint(1,30) for i in range(50)]

def bucketsort(data,bucket):

    size = len(data)
    aux = [[] for i in range(size//bucket)]
    aux_2 = []
    for i in data:
        aux[i//bucket].append(i)
    for i in range(0,(size//bucket)):
        aux[i]=sorted(aux[i])
    for i in range(0, len(aux)):
        for j in range(0,len(aux[i])):
            aux_2.append(aux[i][j])
    return aux_2
data= bucketsort(data, 5)
print(data)