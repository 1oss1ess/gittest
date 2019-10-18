def decorator_function(original_func):
    def wrapper_function(*args, **kwargs):
        return original_func(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print('display function ran')


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments({}, {})'.format(name, age))


display_info('Josif', 22)
display()
