
from sort_c      import bubblesort_caller
from sort_cython import bubblesort as cy_sort
from sort_python import bubblesort as py_sort
import matplotlib.pyplot as plt
import random
import timeit
import array
import create_plot
import numpy as np

def compare_code(n:list):
    t1 =[]
    t2=[]
    t3=[]
    ms_in_sec = 1000

    for i in n:
        unsort = [random.randint(0,i) for _ in range(i)]
        
        arr1 = array.array('i', unsort)
        dur = timeit.timeit(lambda: bubblesort_caller.c_sort(arr1,i), number=1)
        print(f"C[{i}]:", round(dur * ms_in_sec, 1), "ms")
        t1.append(dur)
        
        dur = timeit.timeit(lambda: cy_sort.bubbleSort(arr1), number=1)
        print(f"Cython[{i}]:", round(dur * ms_in_sec, 1), "ms")
        t2.append(dur)
        
        dur = timeit.timeit(lambda: py_sort.bubbleSort(unsort), number=1)
        print(f"Python[{i}]:", round(dur * ms_in_sec, 1), "ms")
        t3.append(dur)

    create_plot.save_plot(n,("C","Cython","Python"),(t1,t2,t3))




n = [100, 200,300, 400,]
compare_code(n)
# n = [ 500, 1000, 2000,4000]
# compare_code(n)