import os


def most_important_function():
    print('This is my intermediate program')


print(__name__)


def main():
    print(os.listdir('/'))
    print('Hello World')


if __name__ == '__main__':
    main()
