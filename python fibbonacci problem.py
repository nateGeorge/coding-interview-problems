from timeit import timeit

def fib(x):
  a, b = 0, 1
  for i in range(x-1):
    #print(a)
    a, b = b, a+b
  
  return b

def rec_fib(n):
    '''inefficient recursive function as defined, returns Fibonacci number'''
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
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