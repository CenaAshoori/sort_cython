import bubblesort 
import random
import timeit

import create_plot

# def bsort(arr, size):
#     for i in range(size-1):
#         sorted = True
#         for j in range(size-i-1):
#             if arr[j] > arr[j+1]:
#                 sorted = False
#                 temp = arr[j+1]
#                 arr[j+1] = arr[j]
#                 arr[j] = temp
#         if sorted:
#             break

def jangolak(size):
    f = 0
    for i in range(size-1):
        f += i
        f -= i

ms_in_sec = 1000
n = [2000000, 4000000]#, 300, 400, 500, 1000, 2000, 4000, 8000]

# t1 = [100, 200, 300, 400, 500, 1000, 2000, 4000, 8000]
# t2 = [11,30,32,222,111,33,444,134,555]
t1 =[]
t2=[]
# unsort = [random.random() for _ in range(1000)]
# print(unsort)
# bubblesort.bsort(unsort,1000)


for i in n:
    unsort = [random.random() for _ in range(i)]
    dur = timeit.timeit(lambda: bubblesort.bsort( i), number=1)
    print(f"Cython[{i}]:", round(dur * ms_in_sec, 1), "ms")
    t1.append(dur)
    
    dur = timeit.timeit(lambda: jangolak( i), number=1)
    print(f"Python[{i}]:", round(dur * ms_in_sec, 1), "ms")
    t2.append(dur)

print (t1)
print (t2)
create_plot.save_plot(n,t1,t2)

