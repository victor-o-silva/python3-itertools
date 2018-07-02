import itertools

"""
    Given a list of values inputs and a positive integer n, write a function that splits inputs into groups of length n.
    For simplicity, assume that the length of the input list is divisible by n. For example, if
    `inputs = [1, 2, 3, 4, 5, 6]` and `n = 2`, your function should return `[(1, 2), (3, 4), (5, 6)]`.
"""


def naive_grouper(inputs, n):
    """Too much memory and time consumption."""
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]


def better_grouper(inputs, n):
    """Better, but discards trailing, unmatched values."""
    iters = [iter(inputs)] * n
    return zip(*iters)


def final_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return itertools.zip_longest(*iters, fillvalue=None)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(naive_grouper(nums, 3))
print(list(better_grouper(nums, 3)))
print(list(final_grouper(nums, 3)))
