def plusOne(digits):
    """
    Take in a large number represented as a 
    List[int] and return +1 in a form of List[int]
    
    time complexity: O(n), worst case each element is processed once 
    space complexity: O(1), in-place modification
    
    :type digits: List[int]
    :rtype: List[int]
    """
    digitsLen = len(digits)
    
    for i in range(digitsLen - 1, -1, -1):
    
        if digits[i] < 9:
            digits[i] += 1
            return digits
        
        digits[i] = 0
        
        
    return [1] + digits


tests = [
    [1,2,3],
    [9,9,9],
    [1,9,9],
    [],
    
]
for i in tests:
    print(f"input: {i} -> output: {plusOne(i[:])}")