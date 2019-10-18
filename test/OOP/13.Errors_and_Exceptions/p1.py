def main():
    try:
        a = 1
        b = 0
        c = a / b
        print('DEBUG: We are here')
    except ZeroDivisionError as err:
        print('Error: {0}'.format(err))
        print('Running the code for Division by zero')
    except TypeError as err:
        print('Error: {0}'.format(err))
        print('Running the code for Thype Error')
    except Exception as err:
        print('Error: {0}'.format(err))
        print('Running the code for general exception')


if __name__ == '__main__':
    main()
