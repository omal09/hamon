import math
 
def isprime(n):
    if n%2 == 0 or n%3 == 0 or n%5==0:
        return False
    for i in range(7, math.floor(math.sqrt(n)), 2):
        if n%i == 0:
            return False
    return True
