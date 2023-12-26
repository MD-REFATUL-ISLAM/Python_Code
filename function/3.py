# def is_prime(n):This line defines a function named is_prime
# that takes an argument n.
def is_prime(n):

    # Checks if the number n is either 2 or 3. 
    # If it is, it returns True since 2 and 3 are prime numbers.
    if n in [2,3]:

        return True
    
    # Checks if the number is equal to 1 or if it's an even number (divisible by 2).
    # If either condition is true, it returns False because
    # prime numbers cannot be less than 2 or even (except for 2 itself).
    if (n == 0) or (n % 2 == 0):

        return False
    # initialize a varibale.
    r = 3
    #  This sets up a while loop that continues as long as
    # the square of r is less than or equal to n.
    # This optimization reduces the number of iterations necessary for finding divisors.
    while r * r <= n:

        if n % r == 0:

            return False
        # Increments r by 2 in each iteration to check only odd numbers as potential divisors
        # (except for 2, which has already been accounted for).
        r = r + 2

    return True

print(is_prime(101),is_prime(99),is_prime(111))
