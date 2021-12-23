from cpython cimport array
import array

cdef extern from "bubblesort.c":
    void sort(int* arr, int size)

cpdef c_sort(array.array arr, int size):
    sort(arr.data.as_ints, size)