def empty_func():
    pass

# asterisk
def print_args(arg1, arg2, *args):
    print('args: ', args)

# two asterisk (keyword arguments)
def print_kwargs(**dic):
    'this docstrings'   #docstrings
    print('dic: ', dic)

print_args(1, 2, 3, 'hello')
print_kwargs(dessert='macaroom', wine='merlot', entree='mutton')

# docstrings
help(print_kwargs)
print(print_kwargs.__doc__)
