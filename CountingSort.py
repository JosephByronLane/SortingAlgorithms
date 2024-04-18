from random import randint
data = [randint(0,5) for i in range(10)]

def counting_sort(data):
    counted = []
    sortedarr = []
    maxSize=len(data)
    maxValue = 0
    for i in range(0,maxSize):
        if data[i] > maxValue:
            maxValue = data[i]
    for i in range(0,maxValue+1):
        counted.append(0)
    for i in range(0, maxSize):
        counted[data[i]] += 1
    for i in range(0,maxValue):
        if counted[i]>0:
            for a in range (0, counted[i]):
                sortedarr.append(i)
    return sortedarr


def countingSort_dict(data):
    values={
    }
    lowbound=min(data)
    highbound=max(data)
    sortedarr=[]
    for i in range(lowbound, highbound+1):
        values[i]=0
    for i in data:
        values[i]+=1
    for i in range(lowbound,highbound+1):
        if values[i] > 0:
            for a in range(0, values[i]):
                sortedarr.append(i)
    return sortedarr


def countingSort_dict_remastered(data):
    #KEY:VALUE
    values = {
    }
    minvalue = min(data)
    maxvalue=max(data)
    sortedarr=[]
    for i in data:
        if i not in values:
            values[i] = 1
        elif i in values:
            values[i]+=1
    for i in range(minvalue,maxvalue+1):
        if i in values:
            for a in range(0, values.get(i)):
                sortedarr.append(i)
    return sortedarr

print(data)
data = counting_sort(data)
print(data)

