def queue_time(customers, n):
    """
    return the total time of checkout given list of customers timen and n tills
    
    time complexity: O(m * n), where m is number of customers.
                     For each coustomer, min(tills) and .index() scan n times
                     
    space complexity: O(n), where n is the numbers of till and 
                      storing the total running time of each till
    
    :type customers: List[int]
    :type n: int
    :rtype: int
    
    """
    tills = [0] * n
    
    for customer in customers:
        smallest_till = tills.index(min(tills))
        tills[smallest_till] += customer
        
    return max(tills)

print(queue_time([], 2)) 
print(queue_time([5, 3, 4], 1))     
print(queue_time([10, 2, 3, 3], 2)) 
print(queue_time([2, 3, 10], 2)) 
   