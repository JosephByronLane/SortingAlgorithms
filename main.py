def mergesort(data):
    if len(data)>1:
        mid = len(data)//2
        subarr1=[]
        subarr2=[]
        for i in range(0,mid):
            subarr1.append(data[i])
        for i in range(mid,len(data)):
            subarr2.append(data[i])

        mergesort(subarr1)
        mergesort(subarr2)

        pointer1 = 0
        pointer2 = 0
        pointer3 = 0

        n1 = len(subarr1)
        n2 = len(subarr2)

        while(pointer1 < n1 and pointer2 < n2):
            if (subarr1[pointer1] <= subarr2[pointer2]):
                data[pointer3] = subarr1[pointer1]
                pointer1+=1
            else:
                data[pointer3] = subarr2[pointer2]
                pointer2+=1
            pointer3+=1

        while (pointer1 <  n1):
            data[pointer3] = subarr1[pointer1]
            pointer1+=1
            pointer3+=1

        while(pointer2 <n2):
            data[pointer3] = subarr2[pointer2]
            pointer2+=1
            pointer3+=1

data = [6, 5, 12, 10, 9, 1]
#startmergesort(data,0,len(data)//2)
mergesort(data)
print(data)