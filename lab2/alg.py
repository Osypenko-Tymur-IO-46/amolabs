def sort(array):
    stepCount = 0
    for i in range(len(array)):
        cMin = i
        for j in range(i+1, len(array)):
            stepCount += 1
            if array[j]<array[cMin]:
                cMin = j
        if cMin!=i:
            array[i], array[cMin] = array[cMin], array[i]
            stepCount += 1
    return stepCount

#test

#array = [1, 18, 92, 17, 15, 60]
#arr1 = sort(array)
#for i in range(len(arr1)):
#    print(arr1[i])