from random import randint
data = [randint(1,10) for i in range(20)]

def combsort(data):
    size = len(data)
    shrink = 1.3
    swap = True
    spaces = size
    while spaces > 1 or swap == True:
        spaces /= shrink
        swap = False
        for i in range(0, int(size-spaces+1)):
            if data[i] > data[int(i+spaces)]:
                data[i], data[int(i+spaces)] = data[int(i+spaces)] , data[i]
                swap = True
    return data
print(data)
data=combsort(data)
print(data)