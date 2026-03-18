def add_binary (a, b):
    """
    Parameter:
    int a - number of the first addition
    int b - number of the second addition
    Output:
    return result - a string version of the sum in baranry
    """
    
    sum = a + b
    result = ""

    while sum > 0:
        reminder = sum % 2
        result = str(reminder) + result
        sum = sum // 2

    return result
