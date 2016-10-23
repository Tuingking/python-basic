''' Decorator - Stack
=========================================================================================================
Use more than one decorator to 'original_function'

NOTE:
    - ORDER matter


'''
from functools import wraps

def my_logger(original_function):
    import logging
    logging.basicConfig(filename='../log-files/{}.log'.format(original_function.__name__), level=logging.INFO)

    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        logging.info('{} ran with args: {}, and kwargs: {}'.format(original_function.__name__,args, kwargs))
        return original_function(*args, **kwargs)
    
    return wrapper_function

def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print "{} ran  in : {} sec".format(original_function.__name__, t2)
        return original_function(*args, **kwargs)
    return wrapper_function

import time

@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print "display_info ran with arguments ({}, {})".format(name, age)
    
display_info('John', 25)

display_info = my_timer(display_info)
print display_info.__name__

''' Same like:
display_info = my_logger(my_timer(display_info))
'''