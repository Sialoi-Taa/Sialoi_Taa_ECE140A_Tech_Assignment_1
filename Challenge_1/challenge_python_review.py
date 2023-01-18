import math

# Question 1
def print_squares():
    ''' Takes no parameters.
        Returns the squared values of numbers 1 - 10 (inclusive).
    '''
    # List comprehension that stores the squared numbers from 1 to 10.
    x = [a**2 for a in range(1, 11)]
    return x

# Question 2
def average(list_of_numbers):
    ''' Takes in a list of numbers.
        Returns the average of those numbers. If the list 
        includes anything other than numbers, the function
        will return nothing. To handle invalid approaches
        I used a try and except method that will catch
        invalid data types being passed into function as
        an argument. I then used a for loop and iterated
        through the elements to catch for any elements
        that aren't of data types int or float.
    '''
    # A try and except block will check if there's any invalid types trying
    # to be passed.
    try:
        # If the list is empty.
        if len(list_of_numbers) == 0:
            return 0
        # If the list isnt all numbers.
        for elem in list_of_numbers:
            if (type(elem) != int) and (type(elem) != float):
                return
    except TypeError:
        return

    # Take the sum of the elements and divide by the number of elements.
    # Then store it in avg.
    avg = sum(list_of_numbers)/len(list_of_numbers)
    return avg

# Question 3
def is_prime(prime):
    ''' Takes in positive integers.
        My method of finding out whether the number
        placed as an argument is a prime number is
        by using modulo to see which number from 0
        to a max number will go into the argument
        with none remaining. I determine the max
        number by iterating from 0 to the argument
        number and seeing when along the way to the
        argument number will the squared product of
        the number of iterations be above that
        number. If the iteration number squared is
        more than the argument, then we return True.
        If the argument passed is 2 or less, then
        the function will return True. If there is
        at any point the argument is found to be 
        divided by the iteration number and there's
        a left over of 0, then the function will
        return False.
    '''
    # A prime number is a natural number greater than 1
    # and is divisible by 1 and itself.
    if prime < 0:
        return

    if prime == 1 or prime == 0:
        return True
    
    # Checks if the argument is divisible by any number
    # with a remainder of 0.
    prime_number = True
    for num in range(2, prime + 1):
        # If the iteration number squared is bigger than the argument,
        # then stop the for loop and return the state of the boolean
        # prime_number.
        if num**2 > prime:
            return prime_number
        else:
            # If the remainder is non-zero, the number is still prime.
            # If the remainder is zero, the number is not prime.
            if not (prime % num):
                return False
    return True

def prime_100():
    ''' Takes no input arguments.
        Keep in mind that a prime number is a
        natural number greater than 1 and is only
        divisible by 1 and itself.
        Will print out the first 100 prime numbers.
        Notice this will not print out the prime
        numbers from 0 to 100, but the first 100
        prime numbers that are found.
    '''
    # Creating a list for the prime numbers to be stored and
    # making variables to track what numbers are being tested
    # for being prime and how many prime numbers are found.
    prime_list = []
    counter = 0
    num = 2

    # A while loop that keeps checking if a prime number is 
    # found and will exit after 100 are found.
    while (counter != 100):
        # if the iteration number is a prime number, add the
        # number to the list of primes and increment the
        # prime counter. 
        if is_prime(num):
            prime_list.append(num)
            counter = counter + 1
        # After each while loop, increment the iteration number 
        # to be tested.
        num = num + 1
    # Returns the list of prime numbers.
    return prime_list

# Question 4
def count_letters(input_string):
    ''' Takes an string input argument.
        This function creates it's own dictionary of
        characters. Each character is connected to a
        number that can be increased at any time. 
        When we iterate through the string, we enter
        the character we're on through the iteration
        processs in the dictionary as a keyword and
        increment the value associated with it.
        After the string is completely iterated
        through, the function returns the dictionary.
    '''
    # This dictionary keeps track of how many times a
    # specific letter was seen.
    dictionary = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0,
        "i" : 0,
        "j" : 0,
        "k" : 0,
        "l" : 0,
        "m" : 0,
        "n" : 0,
        "o" : 0,
        "p" : 0,
        "q" : 0,
        "r" : 0,
        "s" : 0,
        "t" : 0,
        "u" : 0,
        "v" : 0,
        "w" : 0,
        "x" : 0,
        "y" : 0,
        "z" : 0,
        }

    # A for loop that increments the key value pair with
    # the letter seen in the string.
    for elem in input_string:
        # If the character is any type of punctuation,
        # then skip iteration.
        if elem in "!#$%\"&'()*+,-./:;<=>?@[\]^_`{|}~% ":
            continue
        # Places the element at that iteration inside the
        # dictionary key and increments the number
        # associated with it.
        dictionary[elem.lower()] = dictionary[elem.lower()] + 1
    
    return dictionary

# Question 5
def filter_strings(list_of_strings):
    ''' Takes in a list of strings.
        This function will iterate through the list of
        strings and filter out the strings that have 
        contain at least one vowel and are at least 5
        characters long.
    '''
    # This try and except will determin if the list of strings is
    # empty and if true, then the function will return nothing.
    try:
        # Return nothing if the list is empty.
        if len(list_of_strings) == 0:
            return
        # Return nothing if the list has any elements that aren't
        # of the type string.
        for elem in list_of_strings:
            if type(list_of_strings) != str:
                return
    # If there's a type error then return nothing.
    except TypeError:
        return
    
    # I create a list to be returned, a string to help find
    # vowels, and 2 booleans to track conditions for what
    # can be added to the filtered list to be returned.
    filtered_list = []
    vowels = "aeiou"
    vowel_present = False
    character_min = False
    
    # A for loop that filters out the strings that don't
    # meet the requirements to be added to the new list
    # of filtered strings.
    for elem in list_of_strings:
        # Keeps track of how many characters are in a
        # single string.
        char_count = 0
        # This for loop determines if the string should
        # be included with the new list of strings.
        for elem2 in elem:
            # If the string has more than 4 characters
            # and there's a vowel present, break out
            # of the for loop. Else, check if the
            # character is a vowel. If the character is
            # a vowel then change the vowel_present
            # boolean to True.
            if character_min and vowel_present:
                break
            elif elem2.lower() in vowels:
                vowel_present = True
            # Increment the character count
            char_count = char_count + 1
            # If the character count is more than 4 and 
            # the character_min boolean is still False,
            # flip character_min to True.
            if (char_count > 4) and (not character_min):
                character_min = True
        # If both of the booleams are True, then add
        # the string to the filtered list.
        if character_min and vowel_present:
            filtered_list.append(elem)        
        # Resets the booleans after each string has been assessed
        character_min = False
        vowel_present = False
    # Return the filtered list
    return filtered_list

if __name__ == "__main__":
    # Question 1's testing
    print_squares()

    # Question 2's testing
    print(average([3,4,5,6]))
    print(average([-2.3,45,0.111,11/6]))
    print(average([])) # Returns 0
    print(average([1.0,1.0,-math.inf]))
    print(average([1, 3.14, "h"]))
    print(average("hello?"))
    print(average([1,2,3,4].extend([5]))) # what happens here?
    # In the line above me, the argument that gets passed is of type "NoneType"
    # Which doesn't fit into the specified parameters of the function and 
    # because of this invalid input, the function will return nothing as it 
    # has no way of accessing the elements in the list attempting to be passed
    
    # Question 3's testing
    print(prime_100())
    
    # Question 4's testing
    print(count_letters("The quick brown fox jumps over the lazy dog."))
    print(count_letters("Web serving with FastAPI!"))    
    
    # Question 5's testing
    list1 = ["ability", "able", "about", "above", "accept",
            "according", "account", "across", "act", "action"]
    list2 = ["Congress", "consider", "consumer", "contain",
            "continue", "control", "cost", "could", "country"]
    list3 = ["data", "daughter", "day", "dead", "deal", "death",
            "debate", "decade"]
    list4 = ["edge", "education", "effect", "effort", "eight",
            "either", "election"]
    print(filter_strings(list1))
    print(filter_strings(list2))
    print(filter_strings(list3))
    print(filter_strings(list4))