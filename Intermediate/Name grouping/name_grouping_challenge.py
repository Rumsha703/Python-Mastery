from typing import List


def group_names(names:list):

    grouped_names={name[0]:[n for n in names if n.startswith(name[0]) ]for name in names}
    return grouped_names


contacts =  [
    'Emma',
    'Liam',
    'Olivia',
    'Noah',
    'Ava',
    'Isabella',
    'Sophia',
    'Jackson',
    'Lucas',
    'Mia',
    'Charlotte',
    'Harper',
    'Evelyn',
    'Alexander',
    'James',
    'Benjamin',
    'Henry',
    'Ella',
    'Emily',
    'Michael'
]
print(group_names(contacts))