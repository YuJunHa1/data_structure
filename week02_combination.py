def factorial(number) -> int:

    """
    Defines a function that receives an integer value as a parameter and returns a factual calculation result value to an integer.
    :param number: integer
    :return: integer
    """
    result = 1
    for i in range(2, number+1):
        result *= i
    return result

def nCr(n,r) -> int:
    """
    Defines a function that returns the result of the combination by taking over the values of n and r as parameters.
    :param n: a set of n elements
    :param r: r elements
    :return: combination result
    """
    return int(factorial(n) / (factorial(n-r) * factorial(r)))

#print(factorial(int(input())))
n = int(input("input a set of n elements :"))
r = int(input("input r elements :"))
print(f"{n}C{r} = {nCr(n,r)}")