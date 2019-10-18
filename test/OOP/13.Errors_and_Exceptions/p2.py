def main():
    try:
        a = 1
        b = 1
        c = a / b
        print('DEBUG: This line will not be executed')
    except ZeroDivisionError as err:
        print('Error: {0}'.format(err))
        print('Running the code for Division by zero')
    except TypeError as err:
        print('Error: {0}'.format(err))
        print('Running the code for Thype Error')
    except Exception as err:
        print('Error: {0}'.format(err))
        print('Running the code for general exception')
    else:
        print('No have exception')
    print('DEBUG: This line will always be executed')


if __name__ == '__main__':
    main()
