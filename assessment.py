# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def price_with_tax(state, cost, tax=.05):
    """Returns item class including tax given state, cost, and tax rate.

    If user does not specify tax rate, default of .05 is used."""

    if state == 'CA':
        return cost+cost*.07
    #All purchases made in CA are given a tax rate of .07
    else:
        return cost+cost*tax

#price_with_tax('AL', 3.5, .04)
#price_with_tax('CA', 3.5)
#price_with_tax('GA', 3.5)
#Previous lines of code were used to test function in console.  To run additional
#test, change return statments in function to print statements


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

def is_berry(fruit):
    """Given a fruit, returns True if fruit == strawberry, cherry, or blackberry
    and Fasle otherwise"""

    #if fruit == "strawberry" or "cherry" or "blackberry"
    #Above line of code did not run properly, so I wrote three separate if
    #statements.  However, I would like to know if it is possible to use and 
    #or statement within an if statement to make the code more concise
    if fruit == "strawberry":
        return True
    elif fruit == "cherry":
        return True
    elif fruit == "blackberry":
        return True  
    else:
        return False


#is_berry("strawberry")
#is_berry("grape")
#Previous lines of code were used to test function in console.  To run additional
#test, change return statments in function to print statements




#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def shipping_cost(fruit):
    
    def is_berry(fruit):
        if fruit == "strawberry":
            return True
        elif fruit == "cherry":
            return True
        elif fruit == "blackberry":
            return True  
        else:
            return False
#My code did not originally have the above section since I thought I could
#call the is_berry function from within shipping_cost with just the line below.
#However, it would not run unless I redefined the function, so there must be
#a syntax error oc some kind.
    cost = is_berry(fruit)
    if cost == True:
        return 0
    if cost == False:
        return 5

#shipping_cost('strawberry')
#shipping_cost('grape')
#Previous lines of code were used to test function in console.  To run additional
#test, change return statments in function to print statements


# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.

def is_hometown(town_name):
    """Returns True if user gives my hometown (West Palm Beach) as an input. 
    Returns False otherwise."""

    if town_name == "West Palm Beach":
        return True
    else:
        return False

#is_hometown("Miami")
#is_hometown("West Palm Beach")
#Previous lines of code were used to test function in console.  To run additional
#test, change return statments in function to print statements

#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.

def full_name(first, last):
    """Returns a single string with first and last name separated by a single string
    when given first name and last name as two strings"""

    return first+ " " +last

#full_name("Maria", "Mendiburo")
#Previous lines of code were used to test function in console.  To run additional
#test, change return statments in function to print statements

#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def hometown_greeting(town_name, first, last):
    """Returns "Hi, 'user's full name', we're from the same place!" when user gives 
    my hometown (West Palm Beach). Otherwise, returns "Hi 'user full name', where
    are you from?" """

    def is_hometown(town_name):
        if town_name == "West Palm Beach":
            return True

    def full_name(first, last):
        return first+ " " +last

    #I am having the same problem as in 1b.  How can I call a function from within
    #a function without repeating the code?

    hometown_TF_indicator = is_hometown(town_name)
    name_string = full_name(first, last)

    if hometown_TF_indicator == True:
        print "Hi, %s we're from the same place!" (name_string) 

    if hometown_TF_indicator == False:    
        print "Hi, %s, where are you from?" (name_string)

#hometown_greeting("West Palm Beach", "Maria", "Mendiburo")
#I got an error message when I ran the code above.  It indicated a problem in line
#158.  To debug, I tried running it with the name "Maria" in place of the "%s", and
#I removed the (name_string) from the end.  That worked, so I think the problem is 
#with the syntax of the %s.  I did not have time to look up my labs from this week
#where we used the %s.


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def increment(y, x=1):
    def add(y):
        print x + y 

increment(4, 2)
#This is not working properly.  Have tried several variations of what is in the parentheses
#in line 179, including removing y.  That does not work b/c I cannot give the function two
#arguments at the end if I specified only two parameters at the beginning


# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addone with y = 5. Call again with y = 20. 

#Could not get #1 to run, so I had to skip this one

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def append(number, input_list):
    appended_list = input_list.append(number)
    print appended_list

append(4, [3,4,5])
#This does not run properly.  I am getting "None" in my console, which means it
#is returning an empty list.  I tried running it with quotes around all the numbers, 
#but that did not work either.  Even if it did run, it seems like there should be 
#away to specify that input will be a list in the parameter rather than having to 
#use brackets to indicate a list when calling the function.  

#####################################################################