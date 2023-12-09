HW_SOURCE_FILE=__file__


def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    if n==0:
        return n
    elif n%10==8:
        return num_eights(n//10)+1
    else : return num_eights(n//10)


def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777)
    0
    >>> digit_distance(314)
    5
    >>> digit_distance(31415926535)
    32
    >>> digit_distance(3464660003)
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    #1. 此题使用recursive的方法，
    #2. 除了最后一个和第一个数字外，每个数字都被用了两次。
    #3. 对于每个选到的数字，直接减去下一位即可。
    #4. 实质上这个计算公式是abs(n%10-(n//10)%10)
    #5. 注意判断推出递归的条件，当数字内部含有0时，需要注意排除这种特殊情况
    if n>10:
        temp=abs(n%10-(n//10)%10)
        return digit_distance(n//10)+temp
    return 0


def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1 + 2^2 + 3 + 4^2 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1^2 + 2 + 3^2 + 4 + 5^2
    41
    >>> interleaved_sum(4, triple, square) # 1 * 3 + 2^2 + 3 * 3 + 4^2
    32
    >>> interleaved_sum(4, square, triple) # 1^2 + 2 * 3 + 3^2 + 4 * 3
    28
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    """
    #1. 此题需要解决的就怎么构建交替进行的递归。
    #2. 构造两个递归，需要解决什么时候停止进行递归。
    #3. 需要判断输入的数字是什么，奇数的话就从奇函数开始递归，偶数就从偶函数递归.
    #4. 题目限制不能用%来判断奇偶，那么就正向递归。
    def odd_recur(x):
        if x<n:
            return even_recur(x+1)+odd_term(x)
        return odd_term(n)
    def even_recur(x):
        if x<n:
            return odd_recur(x+1)+even_term(x)
        return even_term(n)
    res=odd_recur(1)
    return res

def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def count_coins(total):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
   #1. 此题的含义是通过对不同币值的组合达到total的数值
   #2. 上面定义的函数next_smaller_coin就是为了选择出在total情况下最大的数值
   #3. 看视频来解决这个问题 https://www.youtube.com/watch?v=DvgT4dnSMVM&list=PL6BsET-8jgYVghk6EK4vaIOboLQ-Y9tut&ab_channel=JohnDeNero
    def constrained_count_small(total, largest_coin):
        if total == 0:
            return 1
        if total < 0:
            return 0
        if largest_coin == None:
            return 0
        without_coin = constrained_count_small(
            total, next_smaller_coin(largest_coin))
        with_coin = constrained_count_small(total - largest_coin, largest_coin)
        return without_coin + with_coin
    return constrained_count_small(total, 25)


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    #1. 这个是一个类似于移动的stack上的disk的游戏，就是通过从start的杆开始每次移动一个disk到下一个pole，参考汉诺塔的游戏规则。
    #2. 小圆盘一定在大圆盘之上，也就是start->end的移动必然是比他小的圆盘。参考 https://zhuanlan.zhihu.com/p/94303408
    #3. 做递归类的题目需要了解递归的思想，我们每次都只需要假定f(n)是正确的，不需要知道f(n-1)是怎么计算出来的。
    if n == 1:
        print_move(start, end)
    else:
        other = 6 - start - end
        move_stack(n-1, start, other)
        print_move(start, end)
        move_stack(n-1, other, end)


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return lambda x: x*24


# Test
identity = lambda x: x
square = lambda x: x * x
triple = lambda x: x * 3
interleaved_sum(4, triple, square)
