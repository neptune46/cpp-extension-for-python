import os
from itertools import islice
from random import random
from time import perf_counter

from superfastcode import fast_tanh

COUNT = 500000  # Change this value depending on the speed of your computer
DATA = list(islice(iter(lambda: (random() - 0.5) * 3.0, None), COUNT))

def test(fn, name):
    start = perf_counter()
    result = fn(DATA)
    duration = perf_counter() - start
    print('{} took {:.3f} seconds\n\n'.format(name, duration))

    for d in result:
        assert -1 <= d <=1, " incorrect values"


test(lambda d: [fast_tanh(x) for x in d], '[fast_tanh(x) for x in d]')

os.system("pause")
