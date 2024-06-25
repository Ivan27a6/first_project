def square(a):
    return a ** 2


if __name__ == '__main__':
    if True:
        print(square(3))
    try:
        square(u)
    except:
        print('error')
    finally:
        print('message')
