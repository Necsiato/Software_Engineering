def replace(inputList):
    memory = inputList[0]
    inputList[0] = inputList[-1]
    inputList[-1] = memory
    return inputList

print(replace([1, 2, 3, 4 ,5]))