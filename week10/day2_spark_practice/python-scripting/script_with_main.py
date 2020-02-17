def my_function():
    """
    This is a very important function!
    """
    print('Hello world!')
    print()
    print('This is our name space:')
    print(globals()['__name__'])
    print()
    return 'Good bye!'
    
    
if __name__ == '__main__':
    print('Running script directly:')
    result = my_function()
    print(result)