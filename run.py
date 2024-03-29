from sort_c import bubblesort_caller
from sort_cython_non_optimaze import bubblesort as cy_sort_non
from sort_cython import bubblesort as cy_sort
from sort_python import bubblesort as py_sort

import random
import timeit
import array
import create_plot

def compare_code(n: list,palett):
    t1, t2, t3, t4 = [], [], [], []
    ms_in_sec = 1000

    for i in n:
        unsort = [random.randint(0, i) for _ in range(i)]

        arr1 = array.array('i', unsort)
        
        # C
        dur = timeit.timeit(lambda: bubblesort_caller.c_sort(arr1, i), number=1)
        print(f"C[{i}]:", round(dur * ms_in_sec, 1), "ms")
        t1.append(round(dur * ms_in_sec, 1))
        
        # Cython
        dur = timeit.timeit(lambda: cy_sort.bubbleSort(arr1), number=1)
        print(f"Cython[{i}]:", round(dur * ms_in_sec, 1), "ms")
        t2.append(round(dur * ms_in_sec, 1))
        
        # Cython - non optimaze
        dur = timeit.timeit(lambda: cy_sort_non.bubbleSort(unsort), number=1)
        print(f"Cython - NON[{i}]:", round(dur * ms_in_sec, 1), "ms")
        t3.append(round(dur * ms_in_sec, 1))
        
        # Python
        dur = timeit.timeit(lambda: py_sort.bubbleSort(unsort), number=1)
        print(f"Python[{i}]:", round(dur * ms_in_sec, 1), "ms")
        t4.append(round(dur * ms_in_sec, 1))
        print()

    create_plot.save_plot(n, ("C", "Cython","Cython-NON", "Python"), (t1, t2, t3,t4),palett)



palett = """
#D8E3E7
#51C4D3
#126E82
#132C33
"""
# n = [100, 200, 500, 1000]
# compare_code(n,palett)
n = [2000, 3000, 5000,7000]
compare_code(n,palett)
