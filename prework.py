# Question 1
# Write a funtion to print "hello_USERNAME!" USERNAME is the unput of the function.

def hello_name(user_name):
    '''Print hello_USERNAME.'''
    print('hello_' + user_name.upper() + '!')

hello_name('username')

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    '''Print odd numbers 1-100, but return nothing.'''
    y = True
    if y == True:
        start, end = 0, 100
        for num in range(start, end + 1):
            if num % 2 != 0:
                print(num, end=' ')
    else: 
        print(' ')
    
first_odds()

# Question 3 
# Please write a Python function, max_num_in_list to return the max number of a given list.
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    '''Print the max number of a given list.'''
    print(max(a_list))

max_num_in_list([1,3,5,33,66,234,5567,1,32])

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4,
# but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type(true/false)

def is_leap_year(a_year):
    '''Return given year is a leap year or not.'''
    if (a_year % 400 == 0) and (a_year % 100 == 0):
        print(True)
    elif (a_year % 4 ==0) and (a_year % 100 != 0):
        print(True)
    else:
        print(False)

is_leap_year(2004)

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean type.

def is_consecutive(a_list):
    '''Check to see if all number in list are consecutive'''
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

some_list= [1,3,2,4,6]
print(is_consecutive(some_list))
