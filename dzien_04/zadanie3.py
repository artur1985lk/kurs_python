def policz_znaki(value: str, start: str="<", end: str= ">") -> int:
    """

    :param value:
    :param step:
    :return:
    >>> policz_znaki('ala ma <kota> a kot ma ale')
    4
    >>> policz_znaki('ala ma <kota> a <kot> ma ale')
    7
    >>> policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']')
    18
    >>> policz_znaki('ala [kota [a kot]] ma [ale]', start='[', end=']')
    18
    >>> policz_znaki('a <a<a<a>>>')
    6
    """
    count = 0
    s = 0
    znak = 0
    for i in value:
        x = 1

        if i == start:
            znak += 1
            s = True
            if i == "[" or "<":
                x += 1
            if i == "]" or ">":
                x -= 1
        if s == True:
            count += (1 * x)
        if i == end:
            znak += 1
            s = False



    return count - znak


# x = "ala ma <kota> a kot"
# print(policz_znaki(x))
# print(help(policz_znaki()))