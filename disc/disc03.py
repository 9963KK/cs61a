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
        return 1
    elif n%2==0:
        return hailstone(n//2)+1
    else:
        print(n)
        return hailstone(n*3+1)+1


def merge(n1, n2):
    """Merges two numbers by digit in decreasing order.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    #1. 在内部定义一个递归函数，对于n1和n2分别起效即可。
    #2. 最后在结束时对二者所得到的list进行排序输出即可。
    #3. 内部子函数有个问题，NoneType没法传出来,即append传出来的是None，
    # def split(n):
    #     if n==0:
    #         n_list=[]
    #         return n_list
    #     else:
    #         temp=n%10
    #         n//=10
    #     return split(n)+[temp]
    # n1_list,n2_list=split(n1),split(n2)
    # n_list=n1_list+n2_list
    # n_list.sort(reverse=True)
    # res=''.join(str(x) for x in n_list)
    # return int(res)
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10

# def split(n):
#     if n == 0:
#         n_list = []
#         return n_list
#     else:
#         temp = n % 10
#         n //= 10
#     return split(n).append(temp)
