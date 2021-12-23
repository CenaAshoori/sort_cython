import cython
def bsort(size: cython.int):
    f: cython.int = 0
    for i in range(size-1):
        f += i
        f -= i
