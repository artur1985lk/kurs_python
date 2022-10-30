def max_of_tree(x, *args):
    max = x
    for i in [x, *args]:
        if i > max:
            max = i
    return max

# max = lambda max:
# print(max_of_tree(2, 6, -5, 3, 7, 2))

if __name__ == "__main__":
    assert max_of_tree(1, 3, 2) == 3
    assert max_of_tree(2, 6, -5) == 6
