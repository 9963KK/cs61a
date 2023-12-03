from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    #1. 既然此题是要求增序，那么倒过来就是降序。
    #2. 此时基础的数就要设为9
    i=9
    while i>=x%10:
        i,x=x%10,x//10
        if x==0: return True
    return False

def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    #1. 此题首先需要确定有几个增长序列在n中。
    #2.提取出增长序列，假设有a个不同的序列，对这些序列进行排序，按照顺序来。
    #3.题目中限制了几个变量的使用。
    #4. 考虑k=0的情况，同时考虑中间数字相同时也需要截断。在遍历到最后一个数字时，会出现0的情况，需要避免
    i = 0
    final = None
    while i<=k:
        while True:
            temp=n%10
            n=n//10
            if temp<=n%10 or n%10==0:
                break
        final = temp
        i = i+1
        n = n
    return final


def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0

    """
    power_of_two = 1.0
    #1. 首先确定要选的幂次方是多少，可以设置一个数val，当pow(2,val)>x时，即可以将其纳入考虑范围。
    #2. 分别的对val和val-1进行测试
    #3. 对于小于1的数，需要特殊处理,从负次幂的角度来计算。
    val=0
    if x<1 and x>0:
        while pow(2,val)>x:
            val=val-1
        if abs(pow(2,val)-x)<abs(pow(2,val+1)-x):
            power_of_two=pow(2,val)
        else:
            power_of_two = pow(2, val+1)
    elif x>=1:
        while pow(2,val)<x:
            val=val+1
        if abs(pow(2,val)-x)<abs(pow(2,val-1)-x):
            power_of_two=pow(2,val)
        else: power_of_two=pow(2,val-1)
    else: power_of_two=None
    return power_of_two


def make_repeater(func, n):
    """Returns the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
   #1. 我需要返回的是一个递归的函数
   #2. 传入递归的次数
   #3. 思路类似于add_three(5)->make_repeater(increment,3)(5)->func_recursive(5)->res
   #4. 每次要递归的次数是固定的，实质上就是怎么把递归的次数传入内置函数。验证的条件是counter==0时的情况,注意再内置counter=n时，每次递归都会使counter的值重置。
    if n==0: return lambda x:x
    def func_recursive(x,counter=n):
        if counter==1:
            return func(x)
        else:
            counter-=1
            return func(func_recursive(x, counter))
    return func_recursive

def composer(func1, func2):
    """Returns a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f

def apply_twice(func):
    """Returns a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    return lambda x: composer(func,func)


def div_by_primes_under(n):
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    checker = lambda x: False
    i = ____________________________
    while ____________________________:
        if not checker(i):
            checker = ____________________________
        i = ____________________________
    return ____________________________

def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """
    def checker(x):
        return False
    i = ____________________________
    while ____________________________:
        if not checker(i):
            def outer(____________________________):
                def inner(____________________________):
                    return ____________________________
                return ____________________________
            checker = ____________________________
        i = ____________________________
    return ____________________________


# Test session
# get_k_run_starter(123444345, 3)
# add_three = make_repeater(increment, 3)
# add_three(5)
