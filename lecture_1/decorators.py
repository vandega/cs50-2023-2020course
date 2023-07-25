def general(func):
    print('it was here')

    def wrapper():
        print('start of wrapper')
        func()
        print('end of wrapper')

    return wrapper()


@general
def myfunc():
    print('my func')
