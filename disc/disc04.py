#Tree Recursion
# https://cs61a.org/disc/disc04/
"""
def virfib(n):
    if n == 0 or n == 1:
        return n
    return virfib(n - 1) + virfib(n - 2)
"""


def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either one step or two steps at a time.
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(4)
    5
    """
    #1. 这个题目和count_partitions的原理有点像，但是可以利用tree recursion的方法解决
    if n==2 or n==1: return n
    return count_stair_ways(n-1)+count_stair_ways(n-2)


def count_k(n, k):
    """Counts the number of paths up a flight of n stairs
    when taking up to k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    #1. 可以理解为上题目中不再限制每次跨出的步数。
    #2. 理解为递归树上有多少个节点
    #3. 此题和count_partitions类似,但是这个是有顺序的比如说1+2和2+1是不一样的，但在count_partitions中，二者相同。
    #4. 对于每个数来说，都可以依次从1到k不同的数字组合来组成n，都是不一样的组合。
    #5. 公式可以写为count_k(n-1,k)+count_k(n-2,k)+count_k
    """
    We use a loop in our solution for count_k. The first iteration of the loop counts the ways to go up n steps if we start by taking one step, the second iteration counts the ways to go up n steps if we start by taking two steps, and so on. The very last iteration counts the ways to go up n steps if we start by taking k steps, which is the most we can take at once.

We use the total variable to track the sum of the results of our recursive count_k calls. When the loop ends, total will store the number of ways to go up n stairs and will include every possible starting move.

You can use recursion visualizer to step through the call structure of count_k(3, 3).
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        for step in range(1, k + 1):
            total += count_k(n - step, k)
        return total
    # ALTERNATE SOLUTION
def count_k(n, k):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n - i, k)
            i += 1
        return total

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1 or n == 1:
        return 1
    return paths(m - 1, n) + paths(m, n - 1)
    # Base case: Look at the two visual examples given. Since the insect
    # can only move to the right or up, once it hits either the rightmost edge
    # or the upper edge, it has a single remaining path -- the insect has
    # no choice but to go straight up or straight right (respectively) at that point.
    # There is no way for it to backtrack by going left or down.
    # Alternative solution:
    if m == 1 and n == 1:
        return 1
    if m < 1 or n < 1:
        return 0
    return paths(m - 1, n) + paths(m, n - 1)
    # This solution is similar to the alternate solution for Count Stair Ways.
    # If we reach the exact destination, we have found a unique path (first base case), but if
    # we overshoot, we have not found a valid path (second base case).

    # Notice, however, that this solution is not as short and simple as the first solution
    # since it doesn't make use of the insect's restricted movements (only right or up)
    # to cut the program short. We have to reach the exact destination for the second solution,
    # while in the first we just have to reach the right or top boundary.


def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    if len(s) == 1:
        return s[0]
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))
        # OR
        return max(s[0] * max_product(s[2:]), s[1] * max_product(s[3:]))
    """
This solution begins with the idea that we either include s[0] in the product or not:

If we include s[0], we cannot include s[1].
If we don't include s[0], we can include s[1].
The recursive case is that we choose the larger of:

multiplying s[0] by the max_product of s[2:] (skipping s[1]) OR
just the max_product of s[1:] (skipping s[0])
Here are some key ideas in translating this into code:

The built-in max function can find the larger of two numbers, which in this case come from two recursive calls.
In every case, max_product is called on a list of numbers and its return value is treated as a number.
An expression for this recursive case is:

max(s[0] * max_product(s[2:]), max_product(s[1:]))

Since this expression never refers to s[1], and s[2:] evaluates to the empty list even for a one-element list s, the second base case (len(s) == 1) can be omitted if this recursive case is used.

The recursive solution above explores some options that we know in advance will not be the maximum, such as skipping both s[0] and s[1]. Alternatively, the recursive case could be that we choose the larger of:

multiplying s[0] by the max_product of s[2:] (skipping s[1]) OR
multiplying s[1] by the max_product of s[3:] (skipping s[0] and s[2])
An expression for this recursive case is:

max(s[0] * max_product(s[2:]), s[1] * max_product(s[3:]))
    """

def flatten(s):
    """Returns a flattened version of list s.

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> deep = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(deep)
    [1, 2, 3, 4, 5, 6]
    >>> deep                                # input list is unchanged
    [1, [[2], 3], 4, [5, 6]]
    >>> very_deep = [['m', ['i', ['n', ['m', 'e', ['w', 't', ['a'], 't', 'i', 'o'], 'n']], 's']]]
    >>> flatten(very_deep)
    ['m', 'i', 'n', 'm', 'e', 'w', 't', 'a', 't', 'i', 'o', 'n', 's']
    """
    lst = []
    for elem in s:
        if type(elem) == list:
            lst += flatten(elem)
        else:
            lst += [elem]
    return lst
#Test
count_k(3,3)