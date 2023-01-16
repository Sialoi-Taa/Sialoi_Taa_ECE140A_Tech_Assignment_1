# Question 1
def print_squares():
    ''' Takes no parameters
        Returns the squared values of numbers 1 - 10 (inclusive).
    '''
    x = [a**2 for a in range(1, 11)]
    return x

# Question 2
def average(list_of_numbers):
    ''' Takes in a list of numbers
        Returns the average of those numbers.
    '''
    avg = sum(list_of_numbers)/len(list_of_numbers)
    return avg 
