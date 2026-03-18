def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif n >= 10:
        return n * 90
    else:
        return n * 97
    
print(sale_hotdogs(0))
print(sale_hotdogs(1))
print(sale_hotdogs(2))
print(sale_hotdogs(10))
print(sale_hotdogs(11))