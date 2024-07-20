class InvalidInputException(Exception):
    "Raised when number input is lower than or equal to one"
    pass

def isPrime(input):
    if input < 2:
        return False
    for number in range(2, input):
        if input % number == 0:
            return False
    return True

def numerosPrimosLinear(input):
    try:
        if input <= 1:
            raise InvalidInputException
        
        primeNumbers = []

        for num in range(2, input + 1):
            if isPrime(num):
                primeNumbers.append(num)
        
        return primeNumbers
    
    except InvalidInputException:
        print('Invalid input! You must pass a value greater than one.')

def numerosPrimosRecursivo(input, primes=None):
    try:
        if input <= 1:
            raise InvalidInputException
        
        if (primes == None):
            primes = []
        
        if (isPrime(input)):
            primes.append(input)
        
        if (input == 2):
            primes.sort()
            return primes

        return numerosPrimosRecursivo(input-1, primes)
    
    except InvalidInputException:
        print('Invalid input! You must pass a value greater than one.')

#exemplos
print(numerosPrimosRecursivo(10)) #output: [2, 3, 5, 7]
print(numerosPrimosLinear(10)) #output: [2, 3, 5, 7]