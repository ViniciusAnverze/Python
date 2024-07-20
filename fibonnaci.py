class invalidInputException(Exception):
    "Raised when number input is lower than zero"
    pass

def fibLinear(input):
    try:
        if (input < 0):
            raise invalidInputException
        elif (input == 0):
            return 0
        elif (input == 1):
            return 1
        
        previousValue = 0
        value = 1
        
        for iteration in range (2, input + 1):
            value += previousValue
            previousValue = value - previousValue
        return value
        
    except invalidInputException:
        print('Invalid input! You must pass a value equal or greater than zero.')

def fibRecursiva(iteration, previousValue=0, value=1):
    try:
        if (iteration < 0):
            raise invalidInputException
        elif (iteration == 0):
            return 0
        elif (iteration == 1):
            return 1
        elif (iteration == 2):
            return value + previousValue
        
        return fibRecursiva(iteration-1, previousValue=value, value=previousValue+value)
        
    except invalidInputException:
        print('Invalid input! You must pass a value equal or greater than zero.')

#exemplos
print(fibLinear(6)) #output: 8
print(fibRecursiva(6)) #output: 8