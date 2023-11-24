def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    if n<=0|k<1:
        return None
    a=1
    for i in range(k):
        a= a*n
        n=n-1
    return a

def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    #这个地方要提取k的整数倍
    #1. 从0累加，直至大于n
    #2. 需要一个临时变量作为基准数
    #3.需要一个计数器来记录能算出来的数字
    temp=k
    counter=0
    if k>n : return 0
    while n>=k:
        print(k)
        k=k+temp
        counter+=1
    return counter

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    #1. Set a temp parameter to store the total value from all the number and the a to record the dominator
    #2. Divide the number using '/' expression to test if the value is large enough to continue the loop
    #Problem: 1. Need to exclude the case that y=10
    #         2. The expression of temp should be adjusted: need to change the number when y is divided by 10^n
    temp=0
    while True:
        temp = temp+(y % 10)
        y=y//10
        if y==0:
            break
    return temp
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    # Need a list to store how many times the 8 has shown
    a=[]
    #Using a similar way to spilit number like sum_digits function
    while True:
        a.append((n%10))
        n=n//10
        counter=0 #To counter if 8 can show twice in a row
        if n==0:
            break
    for i in range(len(a)):
        #Check if there is any 8 in adjecent.
        if a[i]==8:
            counter+=1
        else:
            #Avoid the case that counter<0 then if the number meets the requirement but counter!=2
            if counter==0:
                continue
            else:
                counter-=1
                # When counter=2, we should break loop immediately
        if counter == 2: return True
    return False

