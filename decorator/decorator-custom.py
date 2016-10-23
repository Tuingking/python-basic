def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print "args: {}".format(args)
        print "kwargs: {}".format(kwargs)
        if kwargs['scope'] != 'profile':
            print "error"
        else:
            return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def edit_user(**payload):
    print "edit user to {} {}".format(payload['name'], payload['scope'])

payload = {
    'name': 'yoko',
    'scope': 'profiles'
}
edit_user(**payload)