def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    if n==0:
        return m
    else:
        return multiply(m,n-1)+m


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    for i in range(2,n):
        if n%2==0:
            return True
        else: return False


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    #1. 此题利用递归会非常简单。
    #2. 最后需要输出总共多少个时，直接+1即可。
    if n==1:
        print(n)
        return n
    elif n%2==0:
        print(n)
        n=n//2
        return hailstone(n)+1
    else:
        print(n)
        n=n*3+1
        return hailstone(n)+1


def merge(n1, n2):
    """Merges two numbers by digit in decreasing order.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1==0 and n2==0: return None
    return None