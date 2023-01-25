from itertools import chain

ONES_LIST = {
    '0': '',
    '1': 'бір',
    '2': 'екі',
    '3': 'үш',
    '4': 'төрт',
    '5': 'бес',
    '6': 'алты',
    '7': 'жеті',
    '8': 'сегіз',
    '9': 'тоғыз',
}

TENS_LIST = {
    '0': '',
    '1': 'он',
    '2': 'жиырма',
    '3': 'отыз',
    '4': 'қырық',
    '5': 'елу',
    '6': 'алпыс',
    '7': 'жетпіс',
    '8': 'сексен',
    '9': 'тоқсан',
}

HUNDREDS_LIST = [
    'жүз',
    'мың',
    'миллион',
    'миллиард',
    'триллион',
]


def two_digit(value: str) -> str:
    return ' '.join(filter(None, [TENS_LIST[value[:1]], ONES_LIST[value[1:]]]))


def three_digit(value: str) -> str:
    hundred = ' '.join(filter(None, [ONES_LIST[value[:1]] if value[:1] != '1' else '', HUNDREDS_LIST[0]]))
    return ' '.join(filter(None, [hundred, TENS_LIST[value[1:2]], ONES_LIST[value[2:]]]))


def transform(value: int) -> str:
    if value == 0:
        return 'нөл'
    negative_prefix = ''
    if value < 0:
        negative_prefix = 'минус'
        value = abs(value)
    value_divided = reversed(f'{value:,}'.split(','))

    reverse_res = []
    for i, value_group in enumerate(value_divided):
        match len(value_group):
            case 1:
                res = ONES_LIST[value_group]
            case 2:
                res = two_digit(value_group)
            case 3:
                res = three_digit(value_group)
            case _:
                raise ValueError(f'Got bad value group: {value_group}')
        if i and len(HUNDREDS_LIST) > i:
            res += f' {HUNDREDS_LIST[i]}'
        reverse_res.append(res)
    return ' '.join(filter(None, chain([negative_prefix], reversed(reverse_res))))


if __name__ == '__main__':
    x = int(input())
    print(transform(x))
