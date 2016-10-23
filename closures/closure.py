# Closures

def outer_func(msg):
    message = msg

    def inner_func():
        print (message)
    
    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()
hello_func()


def outer_func(msg):
    def inner_func():
        print msg
    return inner_func

hi_func = outer_func('hi')
bye_func = outer_func('bye')

hi_func()
bye_func()