''' Decorator
=========================================================================================================
Way to decorate a function:
    add '@decorator_function' exactly above the 'original_function'

By adding '@decorator_function' above the 'original_function' is exactly the same like
    '' display = decorator_function(display) ''

'original_function' is the function that wants to be decorated
in this context:
    original_function could be
        1. display()
        2. display_info()

Common usecase decorator been used:
1. logging: to keep track how many times specific function is run
    example can be seen on 'decorator-logging.py'
2. timer: Keep track how long the function has ran
    example can be seen on 'decorator-timer.py'

The name of the 'original_function' will be change to 'wrapper_function' after decorated
but we can use 'wraps' module from 'functools' to fix this kind of problem, by:
    add '@wraps(original_function)' above wrapper_function of the decorator
example can be seen on 'decorator-stacking.py'
'''


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        """
        remember to put '()' at the end of 'original_function'
        in order to return the value of the function
        not return function
        """
        print "wrapper executed this before {}".format(original_function.__name__)
        print "args: {}".format(args)
        print "kwargs: {}".format(kwargs)
        return original_function(*args, **kwargs) 
    return wrapper_function

@decorator_function
def display():
    print "display function ran"

display()

''' Same like:
display = decorator_function(display)
'''

@decorator_function
def display_info(name, age):
    print "display_info ran with arguments ({}, {})".format(name, age)

display_info('John', 25)