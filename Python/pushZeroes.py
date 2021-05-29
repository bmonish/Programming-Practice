def pushZeroes(input1, input2):
    zeroArray = [] 

    for i in input1:
        if i == 0:
            input1.remove(i)
            zeroArray.append(0)

    input1.extend(zeroArray)
    
    return input1

print(pushZeroes([1,0,4,0,5], 5))