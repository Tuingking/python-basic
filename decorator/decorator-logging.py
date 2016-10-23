def my_logger(original_function):
    import logging
    logging.basicConfig(filename='../log-files/{}.log'.format(original_function.__name__), level=logging.INFO)

    def wrapper_function(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return original_function(*args, **kwargs)
    
    return wrapper_function

@my_logger
def display_info(name, age):
    print "display_info ran with arguments ({}, {})".format(name, age)

display_info('John', 25)


