str_not_empty = lambda n: len(n) > 0


def value_more_than(value: float):
    return lambda n: n >= value


def value_less_than(value: float):
    return lambda n: n <= value
