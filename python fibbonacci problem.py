from timeit import timeit

def fib(x):
    if not isinstance(x, int):
        raise ValueError("x must be an int")
    a, b = 0, 1
    for i in range(x):
    a, b = b, a+b
    return a

def rec_fib(n):
    '''inefficient recursive function as defined, returns Fibonacci number'''
    # the commented lines help understand how the recursion is working
    #print('n=', n)
    if n > 1:
        #print(n-1, n-2)
        return rec_fib(n-1) + rec_fib(n-2)
    #if n == 1:
    #    print('adding 1')
    return n

def mem_fib(n, _cache={}):
    '''efficiently memoized recursive function, returns a Fibonacci number'''
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, mem_fib(n-1) + mem_fib(n-2))
    return n

timeit("fib(20)", setup='from __main__ import fib', number=10)
timeit("rec_fib(20)", setup='from __main__ import rec_fib', number=10)
timeit("mem_fib(20)", setup='from __main__ import mem_fib', number=10)
