def fizz_buzz(num):
    """
    Problem
    For numbers 1 to n
    multiples of 3 → "Fizz"
    multiples of 5 → "Buzz"
    multiples of 3 and 5 → "FizzBuzz"
    Example for n=5
    1
    2
    Fizz
    4
    Buzz
    """
    for n in range (1, num+1):
        if ((n % 3 == 0) & (n % 5 == 0)):
            print("FizzBuzz")
        elif(n % 3 == 0):
            print("Fizz")
        elif(n % 5 == 0):
            print("Buzz")
        else:
            print(n)

fizz_buzz(19)