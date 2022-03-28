# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
# Examples:
#
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
#
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
#

def longest(a: str, b: str):
    #set_a = set(a)
    set_b = set(b)
    set_b.update(set(a))
    return sorted([el for el in set_b]) # sorted(set_b)

def longest_str(a: str, b: str) -> str:
    return ''.join(sorted(set(a + b)))
    