def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    """
    Return a list of numbers within the range [a, b] where each number
    is equal to the sum of its digits raised to consecutive powers
    starting from 1 (Eureka numbers).
    
    time complexity: O(n * d), where n is the number of values in the range
    (b - a + 1) and d is the number of digits in each number. Each number
    is converted to a string and iterated through its digits.
    
    space complexity: O(k), where k is the number of valid Eureka numbers
    stored in the result list.
    
    :type a: int
    :type b: int
    :rtype: List[int]
    """
    return [ num for num in range(a, b +1) if is_eureka(num)]
            
def is_eureka(number):
    """
    Check if a number satisfies the Eureka property.
    A number is valid if the sum of its digits raised to increasing
    powers (starting from 1) equals the original number.
    
    time complexity: O(d), where d is the number of digits in the number.
    
    space complexity: O(d), due to converting the number to a string.
    
    :type number: int
    :rtype: bool
    """
    digits = str(number)
    total = 0
    for i, num in enumerate(digits, start=1):
        num = int(num)
        total += (num ** i)
        
    return total == number
    

print(sum_dig_pow(1,10000))