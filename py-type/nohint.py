import sys


class Person:
    def __init__(self, name, lang):
        self.name = name
        self.lang = lang


def greeting(man):
    print(hello(man.name))


def hello(name = 'nobody'):
    return 'Hello' + name


if __name__ == '__main__':
    p = Person(sys.argv[1], sys.argv[2])
    greeting(p)
