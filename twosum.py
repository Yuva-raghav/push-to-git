def twoSum(a, b):
    n = {} 

    for i, num in enumerate(a):
        if b - num in n:
            return [n[b - num], i]
        n[num] = i

    return [] 
a = [2, 7, 11, 15, 3]
b = 5
print(twoSum(a,b))  
