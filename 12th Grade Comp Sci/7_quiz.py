'''
Question 1
even numbers from 2 to 100 (inclusive) -- use a list comprehension
'''

# Example 1

x = 0
even_numbers = []
while x != 100:
    x += 2
    even_numbers.append(x)


# Example 2

even_numbers = []
for i in range(2,101):
    if i % 2 == 0:
        even_numbers.append(i)



# Example 3 using a List Comprehension

even_numbers = [i for i in range(2,101) if i % 2 == 0]





'''
Question 2 -- return a list of non vowels from a string
'''

def no_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in string:
        if letter not in vowels:
            result.append(letter)

    return result

# USING A LIST COMPREHENSION

def no_vowels(string):
    return [letter for letter in string if letter not in 'aeiou']

'''
Question 3
'''

def list_of_lists(num):
    '''
    This generates a list of num lists containing 1 through num.  Expects integer input
    '''
    my_list = []
    for i in range(1,num + 1):
        my_list.append(i)  # [1, 2, 3, 4]  if num is 4
    result = []
    for i in range(1, num + 1):
        result.append(my_list) #[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

    return result

#OR USING A LIST COMPREHENSION

def list_of_lists(num):
    return [[i for i in range(1, num + 1)] for i in range(1, num + 1)]
  
  
# ANOTHER VARIATION

def list_of_lists(num):
    return [[i for i in range(1, num + 1)]] * num





'''
Question 4
'''

def remove_every_other(lst):
    result = []
    for i in range(len(lst)): # in this line, 'i' will be the index of each element of the list, starting with 0. 
        if i % 2 == 1:       # Here we want to remove every odd index.   If we have index 0,1,2,3,4,5    every other will be 1, 3, 5   which are all odd
            pass
        else:
            result.append(lst[i]) # we will append to result, each element of lst of index i
    
    return result


# OR


def remove_every_other(lst):
    result = []
    for i in range(len(lst)):
        if i % 2 == 0:              # Here we are adding just the even indecies to the list
            result.append(lst[i])   # If in the above example, we removed the odd ones, then we should want to add only the evens 

    return result


# Using a LIST Comprehension

def remove_every_other(lst):
    return [lst[i] for i in range(len(lst)) if i % 2 == 0]



















    
