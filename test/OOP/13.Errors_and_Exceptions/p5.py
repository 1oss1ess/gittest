class Error(Exception):
    pass


class Value_too_small_error(Error):
    pass


class Value_too_large_error(Error):
    pass


def main():
    number = 10
    try:
        i_num = int(input('Please enter an integer:'))
        if i_num < number:
            raise Value_too_small_error
        if i_num > number:
            raise Value_too_large_error
        else:
            print('Perfect!')
    except Value_too_small_error:
        print('The value is too small!')
    except Value_too_large_error:
        print('The value is too large!')
    except Exception:
        print('Unexpected error!')


if __name__ == '__main__':
    main()
