from random import randint
data = [randint(-100,100) for i in range(50)]

def radix_sort(data):

    size = len(data)
    maxnum=max(data)
    idkwhattonamethis=10
    place=10

    howlong = 1
    while maxnum > 1:
        howlong += 1
        maxnum //= idkwhattonamethis
        idkwhattonamethis *= 10
    for i in range(howlong):
        insertion_sort(data, place)
        place*=10


def insertion_sort(data,place):
    n = len(data)
    place2=place//10
    for i in range(1, n):
        aux = data[i]
        j = i - 1
        while j >= 0 and ((aux%place)-(aux%place2)) < ((data[j]%place)-(data[j]%place2)):
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = aux
    return data

radix_sort(data)
print(data)
#
# test2 = 523
# place = 10
# place2 = place/10
# num = (test2%place)-(test2%place2)
# print(int(num))