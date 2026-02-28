def intersection(num1, num2):
    set1 = set(num1)      
    result = set()         
    for x in num2:      
        if x in set1:
            result.add(x)  
    return list(result)
