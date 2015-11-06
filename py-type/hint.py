import sys


class Person:
    def __init__(self, name: str, lang: str) -> None:
        self.name = name
        self.lang = lang


def greeting(man: Person) -> None:
    print(hello(man.name))


def hello(name: str = 'nobody') -> str:
    return 'Hello' + name


if __name__ == '__main__':
    p = Person(sys.argv[1], sys.argv[2])
    greeting(p)

