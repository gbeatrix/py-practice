#!/usr/bin/env python3
#
# Copyright 2023 gbeatrix. All rights reserved.

from itertools import count
from sympy import prime
import timeit

def fibgen(f01):
  if(len(f01) >= 2):
    f0 = f01[-1] + f01[-2]
    f1 = f0 + f01[-1]
  elif(len(f01)==1):
    f0, f1 = 1, 1
  else:
    f0, f1 = 0, 1
  while True:
    yield f0
    f0, f1 = f1, f0+f1

def primes(plist):
    it = count(2) if len(plist)==0 else count(plist[-1]+1)
    it = filter(lambda k: all(k%p>0 for p in plist), it)
    while True:
        p = next(it)
        yield p
        it = filter(lambda k, p=p, min=p*p: k<min or k%p>0, it)

def addcache(generator_function):
  addcache.cache = getattr(addcache, "cache", dict())
  def wrapper(n):
    cache = addcache.cache.setdefault(generator_function.__name__, list())
    if(n<0): raise AttributeError
    if(n<len(cache)):
      return cache[n]
    g = generator_function(cache)
    cache.extend([next(g) for i in range(n+1-len(cache))])
    return cache[-1]
  return wrapper

fib = addcache(fibgen)
nthprime = addcache(primes)

def main():
  for i in range(26):
    print(f"{i =:3}, {fib(i) =:6}, {nthprime(i) =:4}")

  setupstr = """from __main__ import nthprime, addcache
addcache.cache["primes"] = list()"""
  print(f"{'my code':>10}", f'{timeit.timeit("nthprime(130) and nthprime(15000)",setupstr, number=3000):9.4f}', f"{nthprime(130):>9}", f"{nthprime(15000):>9}")
  print(f"{'sympy':>10}", f'{timeit.timeit("prime(131) and prime(15001)","from sympy import prime",number=3000):9.4f}', f"{prime(131):>9}", f"{prime(15001):>9}")
  print(f"{'my code':>10}", f'{timeit.timeit("nthprime(15000)", setupstr, number=3000):9.4f}', f"{nthprime(15000):>9}")
  print(f"{'sympy':>10}", f'{timeit.timeit("prime(15001)","from sympy import prime",number=3000):9.4f}', f"{prime(15001):>9}")
  print(f"{'my code':>10}", f'{timeit.timeit("nthprime(150)", setupstr, number=3000):9.4f}', f"{nthprime(150):>9}")
  print(f"{'sympy':>10}", f'{timeit.timeit("prime(151)","from sympy import prime",number=3000):9.4f}', f"{prime(151):>9}")

if(__name__ == "__main__"):
  main()
