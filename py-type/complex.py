# 1 OMIT
from typing import Dict


def inc(d: Dict[str, int]) -> Dict[str, int]:
    for k in d.keys():
        d[k] = d[k] + 1
    return d

print(inc({
    'a': 1,
    'b': 2,
    'c': 3
}))

# 2 OMIT
from typing import Sequence, List, TypeVar

T = TypeVar('T') # Declare type variable

def pick_odd(s: Sequence[T]) -> List[T]:
    len_ = len(s)
    list_ = []  # type: List
    for i in range(0, len_):
        if i % 2 == 1:
            list_.append(s[i])
    return list_

print(pick_odd([0,1,2,3,4,5,6,7]))
print(pick_odd('abcdefg'))

# 3 OMIT
class Human:
    def __init__(self, father: 'Human' = None, mother: 'Human' = None) -> None:
        self.father = father
        self.mother = mother

    def make(self, couple: 'Human') -> 'Human':
        return Human(self, couple)


print(Human())
# 4 OMIT

import inspect
print(inspect.getfullargspec(inc).annotations)
'''
{
    'd': typing.Dict[str, int],
    'return': typing.Dict[str, int]
}
'''
print(inspect.getfullargspec(Human.make).annotations)
'''
{
    'return': 'Human',
    'couple': 'Human'
}
'''

# 5 OMIT