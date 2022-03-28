# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
# Examples
# Valid arrays
#
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
#
# comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:
#
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
#
# Invalid arrays
#
# If, for example, we change the first number to something else, comp is not returning true anymore:
#
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
#
# comp(a,b) returns false because in b 132 is not the square of any number of a.
#
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
#
# comp(a,b) returns false because in b 36100 is not the square of any number of a.
# Remarks
#
#     a or b might be [] or {} (all languages except R, Shell).
#     a or b might be nil or null or None or nothing (except in C++, Crystal, D, Dart, Elixir, Fortran, F#, Haskell, Nim, OCaml, Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift).
#
# If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.
# Note for C
#
# The two arrays have the same size (> 0) given as parameter in function comp.

def comp(arr1=None, arr2=None):
    if arr1 and arr2:
        arr1.sort()
        arr2.sort()
        check = map(lambda x: x**2, arr1)
        check = list(check)
        print(arr2)
        print(check)
        if arr2 == check:
            return True
        else:
            return False
    return None


def comp_2(array1, array2):
    if array1 and array2:
        return sorted([x*x for x in array1]) == sorted(array2)
    return array1 == array2 == []


print(comp_2([], []))
