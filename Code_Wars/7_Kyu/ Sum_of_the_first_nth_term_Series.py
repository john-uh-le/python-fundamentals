def series_sum(n):
    """
    Your task is to write a function which 
    returns the n-th term of the following series, 
    which is the sum of the first n terms of the sequence 
    (n is the input parameter).
    
    Time: O(n)
    Space: O(1)
    
    
    """
    
    if n == 0:
        return "0.00"
    
    total = 0
    
    for i in range(n):
        total += 1 / (1 + (3 * i))
        
    return total