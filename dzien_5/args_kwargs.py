def sumy(*args, **kwargs):
    x = args
    y = kwargs
    result = 0

    for i in x:
        if type(i) == dict:
            i = sum(i.values())
            result += i
        elif type(i) == list or type(i) == tuple or type(i) == set:
            i = sum(i)
            result += i
        else:
            result += i
    # print(sumy([i for i in y.values()]))
    ## result += sumy(**y.values())
    for i in y.values():
        if type(i) == dict:
            i = sum(i.values())
            result += i
        elif type(i) == list or type(i) == tuple or type(i) == set:
            i = sum(i)
            result += i
        else:
            result += i
    return result


print(sumy(1, [1, 1], [1, 2], {1: 2, 2: 3}, a={1, 2, 3}))


# def test():
#     assert sumy(1) == 1
#     assert sumy(1, 2, 3) == 6
#     assert sumy(1, [1, 1], [1, 2], {1: 2, 2: 3}) == 11
#     assert sumy(1, [1, 1], [1, 2], {1: 2, 2: 3}, a={1, 2, 3}) == 17
