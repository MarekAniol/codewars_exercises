# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
#
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(iterable: str or list) -> list:
    new = []
    for i, el in enumerate(iterable):
        if len(iterable) == iterable.count(el):
            new = [iterable[0]]
        if el != iterable[i - 1]:
            new.append(el)
    return new

def unique_in_order_2(iterable: str or list) -> list:
    new = []
    for el in iterable:
        if len(new) == 0 or el != new[-1]:
            new.append(el)
            print(new)
    return new
