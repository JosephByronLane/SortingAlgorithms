from random import randint
data = [randint(1,100) for i in range(20)]
##data = [7,6,8,9,3,2,10,5,1]

def shellSort(data):
    size = len(data)

    gap = (size//2)
    while gap > 0:
        i=0
        j=i+gap
        while j < size:
            for a in range(gap):
                if data[i] >data[j]:
                    data[i], data[j] = data[j], data[i]
                i+=1
                j=i+gap
                if i >= size or j >= size:
                    break
        gap -= 1
    return data

shellSort(data)
print(data)


























