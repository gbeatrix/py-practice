#!/usr/bin/env python3

import inflect
import timeit

size = 10000
igen = inflect.engine()
data = dict()
for i in range(1, size):
    data[igen.number_to_words(i)]=i

def generate_attempts(pattern):
    results = set()
    length = len(pattern)
    i = length
    j = 0
    while i>0 and i+j <= length:
        result = pattern[j:j+i]
        if result not in results:
            yield result
            results.add(result)
        if i+j == length:
            j = 0
            i = i-1
        else:
            j = j+1

def first(pattern, datadict):
    attempts = generate_attempts(pattern)
    it = filter(lambda attempt: attempt in datadict, attempts)
    try:
        key = next(it)
        val = datadict[key]
        return (key, val)
    except StopIteration:
        return None

def second(pattern, datadict):
    attempts = tuple(generate_attempts(pattern))
    it = filter(lambda key: key in attempts, datadict)
    try:
        key = next(it)
        val = datadict[key]
        return (key, val)
    except StopIteration:
        return None

def main():
    reps = 5000
    patterns = ("fiftyfive", "fifty-five", "five hundred and fifty", "five thousand", "''", "there is one number here")
    for pattern in patterns:
        print('1st: {:9.4f} {:>25} -> {}'.format(
                timeit.timeit("first(\"{}\",data)".format(pattern),
                              "from __main__ import first, data",
                              number=reps),
                pattern,
                first(pattern,data)))
        print('2nd: {:9.4f} {:>25} -> {}'.format(
                timeit.timeit("second(\"{}\",data)".format(pattern),
                              "from __main__ import second, data",
                              number=reps),
                pattern,
                second(pattern,data)))

if __name__=="__main__":
    main()
