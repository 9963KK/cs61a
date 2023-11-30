def composer(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2          # squares x [returns x^2]
    >>> a1 = composer(square, add_one)   # (x + 1) ** 2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = composer(mul_three, a1)     # ((x + 1) ** 2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2          # squares x [returns x^2]
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1) ** 2 == 0 ** 2 + 1
    True
    >>> b1(4)                            # (4 + 1) ** 2 != 4 ** 2 + 1
    False
    """
    """
    1. 在编写该程序时出现了“TypeError: 'bool' object is not callable”这个报错，我认为应该是：
     if composer(f, g)==composer(g, f):
        return True
       这段代码中返回的值被当作一个callable函数来使用了，但实际上，他返回的是True和False whichi is not callable
       所以需要修改代码的结构，之前认为该代码的结构是有问题的。
    2. 在这个函数中，最重要的地方是需要计算composer函数的值是否相等，所以必须要返回的是一个函数，至于是定义函数还是匿名函数都可。
    """
    return lambda x: True if composer(f,g)(x)==composer(g,f)(x) else False


def sum_digits(y):
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total

def is_prime(n):
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_fives = count_cond(lambda n, i: sum_digits(n * i) == 5)
    >>> count_fives(10)   # 50 (10 * 5)
    1
    >>> count_fives(50)   # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4

    >>> is_i_prime = lambda n, i: is_prime(i) # need to pass 2-argument function into count_cond
    >>> count_primes = count_cond(is_i_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    #1. 首先确定该函数需要返回两个参数，分别是n和i
    #2. 要处理的是在增加一个参数后能够处理该额外参数的函数，即可以返回函数
    #3. 可以调用condition函数来解答
    def meet_condition(N):
        #Set a number to counter the number of couples that can meet the condition
        counter=0
        for i in range(1,N+1):
            if condition(N,i):
                counter+=1
        return counter
    return meet_condition
def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    #1. 此题寻找的是最小公倍数，既然a*b是一个公倍数，那么最小公倍数必须小于等于它。
    #2. 最小公倍数multi的范围应该是[max(a,b),a*b]
    #3. 不需要其中的每个数字都遍历，遍历max(a,b)的倍数即可
    basic=max(a,b)
    times=min(a,b)
    i=1
    while True:
        if i==times or (basic*i)%times==0:
            break
        i+=1
    return basic*i


def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    #1. 此题属于函数套函数的方式，首先把cycle设置a(x)函数->b(a(x))(y)->c(b(a(x))(y))(z)
    #2. 返回值必定为函数,而且为high-order function
    #3.需要使用iteration,看进入循环的counter是否大于3然后再想递归那样处理
    # def f4(process):
    #     counter=process
    #     if counter>3:
    #         counter-=3
    #         return f4(counter)
    #     elif counter==0:
    #         return lambda x:x
    #     elif counter==1:
    #         return lambda x:f1(x)
    #     elif counter==2:
    #         return lambda x:f2(x)
    #     elif counter==3:
    #         return lambda x:f3(x)
    #     return
    """
    There are three main pieces of information we need in order to calculate the value that we want to return.

The three functions that we will be cycling through, so f1, f2, f3.
The number of function applications we need, namely n. When n is 0,
we want our function to behave like the identity function (i.e. return the input without applying any of our three functions to it).
The input that we start off with, namely x.
The functions are the parameters passed into cycle.We want the return value of cycle to be a function ret_fn that takes in n and outputs another function ret.
ret is a function that takes in x and then will cyclically apply the three passed in functions to the input until we have reached n applications. Thus, most of the logic will go inside of ret.

Solution:

To figure out which function we should next use in our cycle, we can use the mod operation via %, and loop through the function applications until we have made exactly n function applications to our original input x.
    """
    def g(n):
        def h(x):
            if n == 0:
                return x
            return cycle(f2, f3, f1)(n - 1)(f1(x))
        return h
    return g
#这个地方使用将f1，f2，f3不同的顺序在递归中实现循环使用。

    # def g(n):
    #     def h(x):
    #         i = 0
    #         while i < n:
    #             if i % 3 == 0:
    #                 x = f1(x)
    #             elif i % 3 == 1:
    #                 x = f2(x)
    #             else:
    #                 x = f3(x)
    #             i += 1
    #         return x
    #     return h
    # return g
