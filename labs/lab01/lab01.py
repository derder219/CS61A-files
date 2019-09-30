"""Lab 1: Expressions and Control Structures"""

# Coding Practice

def square(x):

    return x * x

def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    output = x
    counter = n
    if n == 0:
        return output
    else: 
        while counter > 0:
            counter -= 1
            output = f(output) 
        return output

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    a = [int(i) for i in str(n)]
    return sum(a)

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    
    a = [int(i) for i in str(n)]
    cc = len(a) - 1
    if len(a) == 1:
        return False
    else:
        while cc > -1:
            cc -= 1
            if a[cc] == 8 and a[cc+1] == 8:
                return True
        return False
            

