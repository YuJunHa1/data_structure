number = int(input("Input positive number :"))

is_prime = True
if number <2:
    is_prime = False
else:
    i = 0
    while i*i < number:
        if number % i == 0:
            is_prime = False
            break
        print(i, end=' ')
        i += 1
if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")