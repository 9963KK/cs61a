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
    # if n==0: return lambda x:x
    # def func_recursive(x,counter=n):
    #     if counter==1:
    #         return func(x)
    #     else:
    #         counter-=1
    #         return func(func_recursive(x, counter))
    # return func_recursive
    # 没必要使用递归，直接循环也是ok的。
    def inner_func(x):
        k = 0
        while k < n:
            x, k = func(x), k + 1
        return x
    return inner_func

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
    #1. 此题是判断2～n中有没有能被k整除的因数。
    #2. 此题肯定用到了循环这个方法。
    #3. 遍历2～n中的数字来判断if k is divisible
    #4. 其中，使用匿名函数时，注意两个条件：1️⃣只要满足x%i==0和f(x)=True其中之一的条件就可以返回True。2️⃣只有遍历到最后一个时才会同时满足两个都为False的条件。
    checker=lambda x: False
    i = 2
    while i <= n:
        if not checker(i):
            checker = (lambda f, i: lambda x: x % i == 0 or f(x))(checker, i)
        i = i + 1
    return checker
"""
这个题目的理解方式比较特别：
1. 最上面的check(x): return False 是为了保证每一次在对新的i进行x%i操作时，前面的数字没有满足prime条件的。
2. 中间的outer和inner函数，对于每一个不同的i值，都会有对应的outer和inner函数被创造出来。
checker=outer(checker,i)->inner->i=i+1->inner(i+1)->(i+1)%i or checker(i)->inner(i)->inner(i-1)...checker(x): return False
3. 在使用inner函数中 return x%i==0 or func(i) 语句时，前面的是为了确定当前的数字满不满足条件，第二个是为了确定以前的数字满不满足条件。
4. 由于本题限定了必须使用high-order function的写法，不然其实用循环会更简单。但实际上，这题就是希望用high-order function来实现循环的效果，不过写出来的东西很抽象。
5. 推荐使用pythontutor来看一下这个函数的运行过程。https://pythontutor.com/
"""
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
    i = 2
    while i<=n:
        if not checker(i):
            def outer(func,i):
                def inner(x):
                    return x%i==0 or func(i)
                return inner
            checker = outer(checker, i)
        i = i+1
    return checker


# Test session
# get_k_run_starter(123444345, 3)
# add