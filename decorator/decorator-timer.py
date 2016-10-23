def my_timer(original_function):
    import time

    def wrapper_function(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print "{} ran  in : {} sec".format(original_function.__name__, t2)
        return original_function(*args, **kwargs)
    return wrapper_function

import time

@my_timer
def display_info(name, age):
    # time.sleep(2)
    print "display_info ran with arguments ({}, {})".format(name, age)
    
display_info('John', 25)