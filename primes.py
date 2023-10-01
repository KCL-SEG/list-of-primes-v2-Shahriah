"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [2]
    counter = 3
    checkPrime = True

    while (len(list) < number_of_primes) and number_of_primes !=0:
        for i in range(2,counter):
            if (counter % i == 0) and (i != counter):
                checkPrime = False
        if checkPrime:
            list.append(counter)
            counter +=1
        else:
            checkPrime = True
            counter+=1
    if number_of_primes <=0:
        raise ValueError
    print(list)
    return list

