"""Q1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
 The first line of the code has been defined as below."""

def hello_name(user_name):
    """ print the user_name in all caps """
    print("hello_" + user_name.upper())

# hello_name("me")  #this is a test run of the function, not needed for the assignment


"""Q2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing"""
def first_odds():
    """print all the odds numbers and return nothing (not just none)"""
    for i in range(1,101,2):
        print(i)
    return "nothing" #return not needed if you just want none for return instead of actually "nothing"
print(first_odds())   #this is a test to make sure it would both print odds and return nothing
                        #without telling it to specifially print nothing, it actually prints "none"


"""Q3: Please write a Python function, max_num_in_list to return the max number of a given list. 
The first line of the code has been defined as below."""

# numbers = [1,19,22,5,-108]  # test list to make sure the function is working correctly.  
def max_num_in_list(a_list):
    """finds the maximum number in list and then returns it as the variable 'maximum'"""
    maximum=max(a_list)
    return maximum

# print(max_num_in_list(numbers))  #test line to make sure it would return the correct value  
 
 
 
 
"""Q4: Write a function to return if the given year is a leap year. 
A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
The return should be boolean Type (true/false)."""

leap_year = True
def is_leap_year(a_year):
    """function determines if a specific year is a leap year"""
    if a_year % 400 == 0:
        leap_year = True
        #print(a_year + " is a leap year") #the print lines are going beyond the assignment
                                            #they use more human language than the boolean return
    elif a_year % 100 == 0:
        leap_year = False
        #print(a_year + " is NOT a leap year")
    elif a_year % 4 == 0 :
        leap_year = True
        #print(a_year + " is a leap year")
    else:
        leap_year = False
        #print(a_year + " is NOT a leap year")
    return leap_year

# print(is_leap_year(2020))  # tested all possible conditions to make sure it works
# print(is_leap_year(2022))
# print(is_leap_year(2100))
# print(is_leap_year(2400))               
 
 


"""Q5: Write a function to check to see if all numbers in list are consecutive numbers. 
For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
The return should be boolean Type."""

# test_list=[4,5,6,7,8,] #this is a test list to test the function

def is_consecutive(a_list):
    """This determines if numbers are consecutive"""
    order = True
    for i in range(len(a_list)-1): # I used 1 less than the numbers of items in the list to iterate
        if a_list[i] != a_list[i+1]-1: #I then used my iteration to mark the position in the list
            order = False
    return order
    
#print(is_consecutive(test_list)) # this is a test to test the function
    